#!/bin/bash
ollama run deepseek-coder &
sleep 5
uvicorn backend.main:app --reload &
streamlit run frontend/app.py