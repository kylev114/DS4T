MyProject/
├── .venv/               # Ignored by Git
├── .gitignore           # Tells Git to ignore .venv, data, and cache
├── requirements.txt     # Library dependencies
├── README.md            # Project overview and setup instructions
│
├── data/                # NEVER track this in Git if it's large
│   ├── raw/             # Original, immutable data
│   └── processed/       # Cleaned data ready for modeling
│
├── notebooks/           # Jupyter Notebooks for exploration/prototyping
│   └── 01_exploration.ipynb
│
├── src/                 # The "Engine Room" (Core Python scripts)
│   ├── __init__.py      # Makes this folder a package
│   ├── data_loader.py   # Scripts to fetch/clean data
│   └── model.py         # Your quantitative/trading logic
│
└── main.py              # The entry point that runs the full workflow