# JFK Records Dataset
 
This repository contains the **JFK Records** dataset, originally sourced from the [National Archives](https://www.archives.gov/research/jfk/release-2025).  
It includes approximately **2,200 PDFs (~63,000 pages)** of declassified government documents related to one of history's most scrutinized events.  
 
The dataset has been **fully downloaded, parsed, cleaned, and summarized** using LLMs. Each page has been processed with **Gemini-2.0-Flash** to extract key insights efficiently.  
 
## Available Data  
- **Raw PDFs**: The original government documents can be easily downloaded with a single script.
- **Extracted Texts**: All PDFs have been converted to plain text and stored in the `texts/` folder.  
- **Summaries**: Each page has been summarized using **Gemini-2.0-Flash** and stored in the `summaries/` folder.  
- **File Structure**: Both `texts/` and `summaries/` contain ~2,200 files, each named after its corresponding PDF.  
 
## Features  
- **Full Dataset Access**: Work with **all ~63,000 pages** of JFK records.  
- **Preprocessed & Summarized**: No need to extract text manually—just start analyzing!  
- **Automated PDF Parsing**: Converts government PDFs into structured text.  
- **Summarization**: Each page is summarized using **Gemini-2.0-Flash**, making it easier to extract key insights.  
- **Real-World NLP Challenge**: Can you use LLMs to discover hidden patterns, anomalies, or overlooked details?  
 
## Prerequisites  
- Python 3.11  
- Conda (for environment management)  
- A Gemini API key (free to obtain)  
 
## Installation  
 
### 1. Clone the Repository  
```bash  
git clone https://github.com/Shaier/JFK_Records.git  
cd JFK_Records  
```  
 
### 2. Set Up the Conda Environment  
Create and activate a Conda environment with Python 3.11:  
```bash  
conda create -n jfk python=3.11  
conda activate jfk  
```  
 
### 3. Install Dependencies  
Install the required Python packages using pip:  
```bash  
pip install -r requirements.txt  
```  
 
### 4. Configure the Gemini API Key  
Obtain your Gemini API key from [Google's Gemini API page](https://ai.google.dev/gemini-api/docs/api-key).  
Then, open `extract.py` and replace `YOUR-API-KEY` on **line 8** with your actual API key.  
 
## Reproducing the Results  
 
If you want to **download and extract the data yourself**, follow these steps:  
 
**1. Download the JFK Records (~6.5GB)**  
```bash  
python download_records.py  
```  
 
**2. Extract and Summarize Text from PDFs**  
```bash  
python extract.py  
```  
 
Now, you can analyze the structured dataset and explore the documents! 🚀  
