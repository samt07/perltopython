#!/usr/bin/env python
# coding: utf-8

# # Perl to Python Code Generator
# 
# The requirement: use a Frontier model to generate high performance Python code from Perl code
# 

# In[ ]:


# imports

import os
import io
import sys
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai
import anthropic
from IPython.display import Markdown, display, update_display
import gradio as gr
import subprocess


# In[ ]:


# environment

load_dotenv(override=True)
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY', 'your-key-if-not-using-env')
os.environ['ANTHROPIC_API_KEY'] = os.getenv('ANTHROPIC_API_KEY', 'your-key-if-not-using-env')


# In[ ]:


# initialize
# NOTE - option to use ultra-low cost models by uncommenting last 2 lines

openai = OpenAI()
claude = anthropic.Anthropic()
OPENAI_MODEL = "gpt-4o"
CLAUDE_MODEL = "claude-3-5-sonnet-20240620"

# # Want to keep costs ultra-low? Uncomment these lines:
# OPENAI_MODEL = "gpt-4o-mini"
# CLAUDE_MODEL = "claude-3-haiku-20240307"


# In[ ]:


system_message = "You are an assistant that reimplements Perl scripts code into a high performance Python for a Windows 11 PC. "
system_message += "Respond only with Python code; use comments sparingly and do not provide any explanation other than occasional comments. "
system_message += "The Python response needs to produce an identical output in the fastest possible time."


# In[ ]:


def user_prompt_for(perl):
    user_prompt = "Rewrite this Perl scripts code in Python with the fastest possible implementation that produces identical output in the least time. "
    user_prompt += "Respond only with Python code; do not explain your work other than a few comments. "
    user_prompt += "Pay attention to number types to ensure no int overflows. Remember to #include all necessary python libraries as needed,\
    such as requests, os, json etc.\n\n"
    user_prompt += perl
    return user_prompt


# In[ ]:


def messages_for(perl):
    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_prompt_for(perl)}
    ]


# In[ ]:


# write to a file called script.py

def write_output(python, file_path):
    # Get the base filename from the path
    base_name = os.path.basename(file_path)
    filename = os.path.splitext(base_name)[0]
    code = python.replace("```python","").replace("```","")
    output_file = f"{filename}.py"
    with open(output_file, "w") as f:
        f.write(code)
    return output_file


# In[ ]:


def stream_gpt(perl, file_path):    
    stream = openai.chat.completions.create(model=OPENAI_MODEL, messages=messages_for(perl), stream=True)
    reply = ""
    for chunk in stream:
        fragment = chunk.choices[0].delta.content or ""
        reply += fragment
        cleaned_reply = reply.replace('```python\n','').replace('```','')
        yield cleaned_reply, None
    yield cleaned_reply, write_output(cleaned_reply, file_path)
        


# In[ ]:


def stream_claude(perl, file_path):
    result = claude.messages.stream(
        model=CLAUDE_MODEL,
        max_tokens=2000,
        system=system_message,
        messages=[{"role": "user", "content": user_prompt_for(perl)}],
    )
    reply = ""
    with result as stream:
        for text in stream.text_stream:
            reply += text
        cleaned_reply = reply.replace('```python\n','').replace('```','')
        yield cleaned_reply, None
    yield cleaned_reply, write_output(cleaned_reply, file_path)


# In[ ]:


def generate(perl_script, model, file_path):
    if model=="GPT":
        for result, file in stream_gpt(perl_script, file_path):
            yield result, file
        yield result, file
    elif model=="Claude":
        for result, file in stream_claude(perl_script, file_path):
            yield result, file
        yield result, file
    else:
        raise ValueError("Unknown model")


# In[ ]:


def execute_perl(perl_code):

    import subprocess
    #print(perl_file)
    #perl_path = r"E:\Softwares\Perl\perl\bin\perl.exe"
    # Run Perl script from Jupyter Lab
    result = subprocess.run(["perl", '-e', perl_code], capture_output=True, text=True)

    # Return the output of the Perl script
    return result.stdout
    


# In[ ]:


def execute_python(code):
    try:
        output = io.StringIO()
        sys.stdout = output
        exec(code)
    finally:
        sys.stdout = sys.__stdout__
    return output.getvalue()


# In[ ]:


css = """
.perl {background-color: #093645;}
.python {background-color: #0948;}
"""

force_dark_mode = """
function refresh() {
    const url = new URL(window.location);
    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""


# In[ ]:


with gr.Blocks(css=css, js=force_dark_mode) as ui:

    gr.HTML("<h2 style='text-align: center; color: white;'> PERL to Python Code Generator</h2>")
    with gr.Row(scale=0, equal_height=True):
        model = gr.Dropdown(["GPT", "Claude"], label="Select model", value="GPT")
        perl_file = gr.File(label="Upload Perl Script:")
        convert = gr.Button("Convert to Python")
        file_output = gr.File(label="Download Python script", visible=False)
    with gr.Row():
        perl_script = gr.Textbox(label="Perl Script:")
        python_script = gr.Textbox(label="Converted Python Script:")        
    with gr.Row():
        perl_run = gr.Button("Run PERL")
        python_run = gr.Button("Run Python")
    with gr.Row():
        perl_out = gr.TextArea(label="PERL Result:", elem_classes=["perl"])
        python_out = gr.TextArea(label="Python Result:", elem_classes=["python"])
    with gr.Row():        
        clear_button = gr.Button("Clear")
    
    def extract_perl_code(file):
        if file is None:
            return "No file uploaded."
        with open(file.name, "r", encoding="utf-8") as f:
            perl_code = f.read()
        return perl_code

    convert.click(extract_perl_code, inputs=[perl_file], outputs=[perl_script]).then(
        generate, inputs=[perl_script, model, perl_file], outputs=[python_script, file_output]).then(
        lambda file_output: gr.update(visible=True), inputs=[file_output], outputs=[file_output]
    )

    perl_run.click(execute_perl, inputs=[perl_script], outputs=[perl_out])
    python_run.click(execute_python, inputs=[python_script], outputs=[python_out]) 

    def clear_all():
        return None, "", "", gr.update(visible=False), "", ""

    clear_button.click(
        clear_all,
        outputs=[perl_file, perl_script, python_script, file_output, perl_out, python_out]
    )

ui.launch(inbrowser=True)


# In[ ]:




