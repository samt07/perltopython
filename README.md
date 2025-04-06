# PERL To Python Code Converter
Upload your PERL script and get Python equivalent optimized for a faster performance. Developed using LLMs (Multi model)

## Features
- User to upload a Perl script and click Convert to Python button.
- Python script will be streamed instantaneously and also will be available for download.
  
## Requirements
To run this project, you need the following:
### For Frontier models GPT and Claude
- Python 3.11 or higher (to run it locally as python script and also for Jupyter Notebook)
- Jupyter Notebook (to run it locally using Jupyter lab)
- Your OpenAI API, Claude API, Gemini API Secret Keys. Get one in few secs from [OpenAi](https://platform.openai.com/settings/organization/api-keys), [Claude](https://console.anthropic.com/settings/keys)
- Google Colab account
### For Open source models
- Hugging Face account with a HF token and an Inference end point for `Code_QWEN` model `Qwen/CodeQwen1.5-7B-Chat`
### To test the app in HuggingFace directly (ONLY for gpt-4o-mini)
- [HuggingFace](https://huggingface.co/spaces/Samhugs07/QuestionAnswersDataset)

## Installation

1. **Clone this repository:**
   Open a terminal and run:
   ```bash
   git clone https://github.com/samt07/question-answer-keys.git

2. **Navigate to the project directory**
    ```bash
    cd question-answer-keys

## Set Up Environment Variables  

1. **Create a `.env` file**  
   - Navigate to the project directory.  
   - Create a new file named `.env`.  

2. **Add the OpenAI API Key**  
   - Open the `.env` file in a text editor.  
   - Add the following line:  
     ```env
     OPENAI_API_KEY=your_openai_key
     ```
   - Ensure:  
     - No spaces before or after the `=`.  
     - No quotes around the value.  

3. **Save the file**  
   - Save it with the exact name `.env`.  
   - Verify that it is not saved as `.env.txt`, `env.env`, or any other variation.  

## Usage

## Option 1: Test the app here [HuggingFace](https://huggingface.co/spaces/Samhugs07/QuestionAnswersDataset) (ONLY for gpt-4o-mini model)

## Option 2: Run with locally installed Jupyter Notebook. You must have installed Python already. 
   1. Create a .env file as mentioned above
   2. Install dependencies
      ```bash
      pip install -qr requirements.txt
   3. Open the Jupyter Notebook:
       ```bash
       jupyter lab question-answer-dataset.ipynb
   4. Follow the instructions in the notebook to execute the code cell by cell, by using `Shift+Enter` key.
   5. If the Python version is 3.13 or higher, there might be a warning message for some imports. These can be ignored.

## Option 3: Run this on Google Colab for Open Source Models.

   1. Go to [Google Colab](https://colab.research.google.com/).  
   2. Click **File > Upload Notebook** and select `question-answer-dataset_colab.ipynb` from your local cloned repository folder.
   3. Set up env variable. Use Google Colab's Keys (typically found on the left side tool bar with a Key image)
      - 3a. Add `HF_TOKEN` as the Secret name and paste your Hugging Face token value. Enable the Notebook access option.
   4. For some of the models like Llama, CodeGemma, you would be required to goto HuggingFace, choose that model and accept their Terms and Conditions/License agreements, which is nothing but accepting that you will NOT use these models for any illegal/harmful purposes.
   5. Choose a T4 GPU (free) as the Runtime resource.
   6. Run the Notebook cell-by-cell by pressing `Shift+Enter`.

## Option 4: Run as a standalone .py python script
   1. If Python is not installed already, install Python 3.11 or higher version from [here](https://www.python.org/downloads/)
   2. Create a .env file as mentioned above.
   3. Install dependenices by running this command
      ```bash
       pip install -qr requirements.txt
   4. Run the following command
      ```bash
       ipython question-answer-dataset.py
   
## File Structure
- `question-answer-dataset.ipynb`: Jupyter notebook to run in locally installed jupyter lab.
- `question-answer-dataset_colab.ipynb`: Jupyter notebook to run in Google Colab.
-  `question-answer-dataset.py`: To run as a standalone python script locally
- `.env`: Environment file for storing the API Keys (not included in the repository).
- `requirements.txt`: Contains the required dependencies.
