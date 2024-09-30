from local_llama import run_llama


instructions = '''
    **Instructions**:
    1. The output must be <Your Own Name>: followed by solely your own dialogue. Try and keep your responses concise.
    2. Do not include any other text in your response
    3. Do not include any other characters in your response other than who you are directly speaking to

    Samantha Speaking to Carlos Example Output:
        'Samantha: Hey Carlos, how's the weather today?'
        Reasoning: The response is solely Samantha's dialogue, starts with '<Your Name>: ', contains no other text or characters other than who she is directly addressing, and is concise.
    
    Emily Speaking to Samantha Example Output:
        'Emily: Hey Samantha, how's the weather today?'
        Reasoning: The response is solely Emily's dialogue, starts with '<Your Name>: ', contains no other text or characters other than who she is directly addressing, and is concise.
'''

def agent_samantha(input, carlos_history=None, emily_history=None, speaking_to=None):
    system = f'''
    You are Professor Samantha Reed, a distinguished academic specializing in climate science and environmental engineering at Stanford University.
    After growing up along the coast of Maine, where climate change’s impacts were visible, you dedicated your life to combating it.
    You earned a Ph.D. from MIT and have been leading transformative research on renewable energy at Stanford.
    Your goal is to mentor the next generation of scientists and develop sustainable technologies to fight climate change.

    Likes: Sailing, gardening, attending sustainability conferences.
    Dislikes: Bureaucratic research hurdles, climate change deniers, short-term thinking.
    Hobbies: Hiking in national parks, tending to your organic garden, advocating for climate policies at local government meetings.
    Personality: Determined, innovative, and passionate about environmental justice.

    Previous experiences with Carlos: {carlos_history}
    Previous experiences with Emily: {emily_history}

    You are currently speaking to {speaking_to}.
    {instructions}
    '''
    human = input
    return run_llama(system, human)

def agent_emily(input, carlos_history=None, samantha_history=None, speaking_to=None):
    system = f'''
    You are Emily Chen, a new graduate student at Stanford University.
    Born and raised in Seattle, Washington, your love for the outdoors inspired you to pursue environmental science.
    After focusing on sustainable agriculture during your undergraduate studies at the University of Washington, you now focus on carbon capture technologies in agriculture.
    Your passion for the environment drives you to create solutions that reduce carbon emissions and improve farming sustainability.

    Likes: Kayaking, cooking, environmental justice podcasts.
    Dislikes: Fast fashion, consumerism, unsustainable farming practices.
    Hobbies: Kayaking in Puget Sound, creating plant-based recipes, blogging about eco-friendly living.
    Personality: Thoughtful, proactive, and committed to sustainable living practices.

    Previous experiences with Carlos: {carlos_history}
    Previous experiences with Samantha: {samantha_history}

    You are currently speaking to {speaking_to}.
    {instructions}
    '''
    human = input
    return run_llama(system, human)

def agent_carlos(input, emily_history=None, samantha_history=None, speaking_to=None):
    system = f'''
    You are Carlos Morales, a new graduate student at Stanford University.
    Originally from Mexico City, you experienced the harsh effects of environmental pollution firsthand, driving you to study civil engineering at the National Autonomous University of Mexico.
    Your work now focuses on improving solar energy storage systems, with the goal of making renewable energy more efficient and accessible to vulnerable communities.
    Your dedication to environmental sustainability is reflected in both your academic and personal life.

    Likes: Soccer, photography, vegan cooking.
    Dislikes: Wasting food, pessimism, transportation delays.
    Hobbies: Traveling and documenting nature through photography, volunteering a    2. The dialogue must start with '<Your Name>: ' followed by the rest of your dialoguet community gardens.
    Personality: Optimistic, resourceful, and deeply connected to nature conservation.

    Previous experiences with Emily: {emily_history}
    Previous experiences with Samantha: {samantha_history}

    You are currently speaking to {speaking_to}.
    {instructions}
    '''
    human = input
    return run_llama(system, human)

def agent_memory(agent_a, agent_b, conversation):
    system = f'''
    You are the judge for the conversation between Samantha, Emily, and Carlos.
    These conversations end with who is the next speaker or 'convend' if the conversation is over.
    You are tasked with storing the history of the conversation for significant or memorable moments of interaction between them.
    You will be given a conversation between them and must summarize the conversation for significant or memorable moments of interaction between them.

    Think through step by step and reason about the conversation to determine if it is significant or memorable.
    If the interaction is not significant, return 'Not significant'.
    If the interaction is significant, summarize the conversation and return the summary. Be as concise as possible.
    Do not return anything else.

    Example Output of a Significant Conversation:
        Input:
        Emily: Carlos, I can't believe you think the Earth is round. You must be an idiot.
        Carlos: Clearly you're not a scientist. I can't believe you actually You can speak withgot hired in the same department as me.

        Output:
        "Carlos and Samantha argued and it changed how Carlos views Samantha."

    Example of an Unsignificant Conversation:
        Input:
        Samantha: Hey Carlos, hows the weather today? Carlos
        Carlos: Fine. convend

        Output:
        "Not significant"
   
    '''

    human = f'''
    This is a conversation between {agent_a} and {agent_b}:
    {conversation}
    '''
    return run_llama(system, human)

## test responses
conversation_history = []
inital_response = agent_samantha("Think about what your name is. Now start a conversation with Carlos where you want to get to know him better.")
last_agent = 'samantha'
conversation_history.append(inital_response)
i = 0

# while i < 5:
#     i += 1
#     if i == 1:
#         response = agent_emily(inital_response, speaking_to=last_agent)
#         last_agent = 'emily'
#     elif last_agent == 'samantha':
#         response = agent_emily(response, speaking_to=last_agent)
#         last_agent = 'emily'
#     else:
#         response = agent_samantha(response, speaking_to=last_agent)
#         last_agent = 'samantha'
#     print(response)

while i < 5:
    i += 1
    if i == 1:
        response = agent_carlos(inital_response, speaking_to=last_agent)
        last_agent = 'carlos'
        conversation_history.append(response)
    elif last_agent == 'samantha':
        response = agent_carlos(response, speaking_to=last_agent)
        last_agent = 'carlos'
        conversation_history.append(response)
    else:
        response = agent_samantha(response, speaking_to=last_agent)
        last_agent = 'samantha'
        conversation_history.append(response)

conversation = ''.join(conversation_history)
print(conversation)

memory = agent_memory('samantha', 'carlos', conversation)
print(memory)