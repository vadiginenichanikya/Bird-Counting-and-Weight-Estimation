The project is designed with a modular architecture in mind.  
The `src/` directory represents planned modular components such as bird detection,
tracking, and weight estimation.

For this prototype submission, the complete processing pipeline is implemented
inside `app/processor.py` to ensure a fully working end-to-end demo within the
given time constraints.

The architecture can be easily extended by moving logic from `processor.py`
into the corresponding modules inside `src/`.
