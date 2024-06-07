import os
import PyPDF2
import json
import traceback


def read_file(file):
    if file.name.endswith('.pdf'):
        try:
            pdf_reader=PyPDF2.PdfFileReader(file)
            text=""
            for page in pdf_reader.pages:
                text=text+page.extract_text()
            return text
        
        except Exception as e:
            raise Exception('Error reading PDF file')
        
    elif file.name.endswith('.txt'):
        return file.read().decode('utf-8')
    
    else:
        raise Exception('Error reading file or file unsupported')
    


def get_table_data(quiz_str):    
    try:
        # convert quiz from str to dict 
        quiz_dict=json.loads(quiz_str)
        quiz_table_data=[]

        # iterate over the quiz dict and extract required info
        for key,value in quiz_dict.items():
            mcq=value['mcq']
            options=" || ".join(
                [
                    f"(option)-> (option_value)" for option, option_value in value['options'].items()
                ]
            )
    except Exception as e:
        raise Exception('Error created Quiz Dictionary')
       
    