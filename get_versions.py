import importlib.metadata
packages = [
    "beautifulsoup4",
    "fastapi",
    "html5lib",
    "jinja2",
    "langchain",
    "langchain-astradb",
    "langchain_core",
    "langchain-google-genai",
    "langchain-groq",
    "lxml",
    "python-dotenv",
    "python-multipart,"
    "selenium",
    "streamlit",
    "undetected-chromedriver",
    "uvicorn",
    "structlog",
]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")

# # serve static & templates
# app.mount("/static", StaticFiles(directory="../static"), name="static")
# templates = Jinja2Templates(directory="../templates")