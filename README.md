# Spike Experiment on PDF Conversion

A simple spike using fastapi and PyMuPDF to support better understanding about the quality of output available for converting PDFs to various other formats.

## Installation

- create and activate Python virtual environment (optional, but always recommended)
- install dependencies: `pip install -r requirements.txt`
- run the server: `uvicorn main:app --reload --port 8500`

## Usage

- Place PDF documents in the `documents` folder
- from the server root (`localhost:8500`), you can explore the documents in the folder to see both the extracted metadata and various renderings of their pages by PyMuPDF