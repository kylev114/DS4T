MyProject/
├── .venv/               # Ignored by Git
├── .gitignore           # Tells Git to ignore .venv, data, and cache
├── requirements.txt     # Library dependencies list
├── README.md            # Project overview and setup instructions
│
├── data/                # NStore finance data
│   ├── raw/             # Original, immutable data
│   └── processed/       # Cleaned data ready for modeling
│
├── notebooks/           # Jupyter Notebooks for exploration/prototyping
│   └── tutorial.ipynb
│
├── src/                 # The "Engine Room" (Core Python scripts)
│   ├── __init__.py      # Makes this folder a package
│   ├── data_loader.py   # Scripts to fetch/clean data
│   └── model.py         # Your quantitative/trading logic
│
└── main.py              # The entry point that runs the full workflow