import subprocess

def run_llama(system, human):
    prompt = f'''
    <|begin_of_text|><|start_header_id|>system<|end_header_id|>
    {system}<|eot_id|>
    <|start_header_id|>user<|end_header_id|>
    {human}<|eot_id|>
    '''
    command = ['ollama', 'run', 'llama3.2', prompt]
    return subprocess.run(command, capture_output=True, text=True).stdout