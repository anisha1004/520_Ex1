from datasets import load_dataset
import pandas as pd
import random

dataset = load_dataset("evalplus/humanevalplus")["test"]


# Pick 10 random tasks
random_tasks = random.sample(list(dataset), 10)

# Convert to DataFrame 
df = pd.DataFrame(random_tasks)[["task_id", "entry_point", "prompt"]]
pd.set_option('display.max_colwidth', None)
print(df)

# Print each prompt 
print("\n--- Prompts ---")
for index, row in df.iterrows():
    print(f"\nTask ID: {row['task_id']}")
    print(f"Entry Point: {row['entry_point']}")
    print("Prompt:")
    print(row['prompt'])
    print("-" * 20)


# Save them locally for reuse
# df.to_json("humanevalplus_10_random.jsonl", orient="records", lines=True, force_ascii=False)
# print("\nSaved 10 random tasks → humanevalplus_10_random.jsonl")