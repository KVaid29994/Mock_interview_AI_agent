import os

# Main folder name
base_dir = "ai_agent_mock_interview"

# Subfolders and their 2 custom files
structure = {
    "agent": ["interview_agent.py", "round_manager.py"],
    "core": ["audio_io.py", "feedback_generator.py", "llm_Service.py", "resume_parser.py"],
    "prompts": ["feedback_prompts.py", "question_prompts.py"],
    "utils": ["config.py"]
}
# Create main folder
os.makedirs(base_dir, exist_ok=True)

# Create each subfolder with __init__.py and files
for folder, files in structure.items():
    path = os.path.join(base_dir, folder)
    os.makedirs(path, exist_ok=True)
    
    with open(os.path.join(path, "__init__.py"), "w") as f:
        f.write(f"# {folder} package\n")
    
    for file in files:
        with open(os.path.join(path, file), "w") as f:
            f.write(f"# {file} - placeholder\n")

# Create 'data/uploads' with __init__.py only
data_path = os.path.join(base_dir, "data")
uploads_path = os.path.join(data_path, "uploads")
os.makedirs(uploads_path, exist_ok=True)

with open(os.path.join(data_path, "__init__.py"), "w") as f:
    f.write("# data package\n")

print("✅ Folder structure created successfully.")