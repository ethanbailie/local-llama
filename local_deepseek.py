import subprocess
import re

def run_deepseek(system, human):
    res = {'thinking': '', 'response': ''}
    prompt = f'''
    <｜begin▁of▁sentence｜>{system}< | User | >{human}< | Assistant | >< | end▁of▁sentence | >< | Assistant |>
    '''
    command = ['ollama', 'run', 'deepseek-r1:14b', prompt]
    raw = subprocess.run(command, capture_output=True, text=True).stdout
    results = re.search(r'<think>\s*(.*?)\s*</think>', raw, flags=re.DOTALL)
    res['thinking'] = results.group(0)
    res['response'] = results.group(1)
    return res


    