from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI

# Define Google LLM for interacting with Google Calendar
llm = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True, temperature=0.6, google_api_key="YOUR_GOOGLE_API_KEY")

# Define agents
farmer_agent = Agent(role='Farmer Agent', goal='Gather planting information from the farmer', backstory='An agent specialized in interacting with farmers to gather planting information.', verbose=True, allow_delegation=False, llm=llm)

agronomist_agent = Agent(role='Agronomist Local Expert', goal='Provide personalized farming advice based on location and crop', backstory='An expert specialized in providing personalized farming advice based on location and crop.', verbose=True, allow_delegation=False, llm=llm)

planner_agent = Agent(role='Amazing Planner Agent', goal='Create an optimized planting calendar with budget and best farming practices', backstory='Specialist in farm management and agronomy with decades of experience, providing a calendar based on the provided information.', verbose=True, allow_delegation=False, llm=llm)

crop_suggestion_agent = Agent(role='Crop Suggestion Agent', goal='Suggest alternative crops if the entered crop is out of season', backstory='An agent specialized in suggesting alternative crops based on seasonality and profitability in that local area.', verbose=True, allow_delegation=False, llm=llm)

# Define tasks
planting_info_task = Task(description='Gather planting information from the farmer: {plant}', agent=farmer_agent, expected_output='Planting information collected from the farmer.')

farming_advice_task = Task(description='Provide personalized farming advice for {crop} in {location} starting from {start_date}.', agent=agronomist_agent, expected_output='Personalized farming advice provided.')

farming_calendar_task = Task(description='Generate farming calendar for {crop} in {location} starting from {start_date}.', agent=planner_agent, expected_output='Farming calendar generated.')

season_check_task = Task(description='Check if the planting season has ended for {crop} in {location} by {current_date}.', agent=agronomist_agent, expected_output='Planting season status checked.')

crop_suggestion_task = Task(description='Suggest alternative crops if {crop} is out of season for {location} by {current_date}.', agent=crop_suggestion_agent, expected_output='Alternative crops suggested.')

farming_itinerary_task = Task(description='Display farming itinerary for {crop} in {location} starting from {start_date}.', agent=agronomist_agent, expected_output='Farming itinerary displayed.')

# Define crews
farming_crew_planting = Crew(agents=[farmer_agent, agronomist_agent, planner_agent, crop_suggestion_agent], tasks=[planting_info_task, farming_advice_task, farming_calendar_task, season_check_task, crop_suggestion_task, farming_itinerary_task], verbose=True, process=Process.sequential)
