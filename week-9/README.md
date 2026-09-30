# Week 9 – Machine Learning, Generative AI and Uncertainty (EGH404)

Lecture and practical transcripts, slides, data and study notes for the Week 9 content. This week introduces machine learning, deep learning and generative AI. It also covers probability pitfalls, meaning independence assumptions and base-rate neglect. The practical covers **Assignment 2, Sections 4 and 5 (locating or synthesising preliminary data)** and runs an Assignment 2 help session.

- [`notes.md`](notes.md) – study notes summarising every transcript and slide deck, grouped by topic.
- [`transcripts/`](transcripts/) – the raw auto-generated transcripts. They are unedited, so expect speech-to-text errors such as "Gase mixture models" for Gaussian mixture models, "Pyros"/"pyro" for PyTorch, and "atom optimizer" for Adam.
- [`slides/`](slides/) – lecture and practical slides.
- `slides/*-ocr.txt` – OCR text of the slide images (code screenshots, rubric tables and figures), because most slides are images with no extractable text.
- [`data/`](data/) – the NASA C-MAPSS turbofan engine data (FD001) used in the Python machine learning example.

## Slides

| File | What it is |
|------|------------|
| [`slides/dealing-with-unpredictability-uncertainty.pdf`](slides/dealing-with-unpredictability-uncertainty.pdf) | "Dealing with Unpredictability": sample spaces, events, probability, independence (the SIDS case and the Monty Hall problem), conditional probability and base-rate neglect. There is no transcript for this deck. |
| [`slides/week-9-practical-genai-data-generation-and-assignment-2-help.pdf`](slides/week-9-practical-genai-data-generation-and-assignment-2-help.pdf) | Week 9 practical: using GenAI to locate public datasets and to generate synthetic data, plus Assignment 2 tips for each section. It goes with transcript 07. |

## Transcripts

### Machine learning concepts

| # | File | Topic |
|---|------|-------|
| 01 | [`01-intro-to-machine-learning-and-deep-learning.txt`](transcripts/01-intro-to-machine-learning-and-deep-learning.txt) | What ML is, training vs testing, applications, supervised/unsupervised/reinforcement learning, feature extraction, deep learning, ChatGPT training, Sora, deepfakes, adversarial attacks |
| 02 | [`02-why-engineers-care-stats-vs-data-mining-vs-ml.txt`](transcripts/02-why-engineers-care-stats-vs-data-mining-vs-ml.txt) | Why engineers need to understand ML tools; statistics vs data mining vs machine learning |
| 03 | [`03-ml-part-2-supervised-unsupervised-and-overfitting.txt`](transcripts/03-ml-part-2-supervised-unsupervised-and-overfitting.txt) | Classification, regression, clustering (k-means, GMMs), dimensionality reduction (PCA, LDA), overfitting |
| 04 | [`04-ml-part-3-data-splits-cross-validation-and-dimensionality.txt`](transcripts/04-ml-part-3-data-splits-cross-validation-and-dimensionality.txt) | Garbage in, garbage out; training/validation/test data; hyperparameters; k-fold cross-validation; the curse of dimensionality |

### Neural networks and generative AI

| # | File | Topic |
|---|------|-------|
| 05 | [`05-neural-networks-and-generative-ai.txt`](transcripts/05-neural-networks-and-generative-ai.txt) | Artificial neurons, deep networks, training with loss and epochs; GenAI milestones (GANs, attention, transformers), how ChatGPT is trained, risks, engineering tools, academic integrity |

### Python example (NASA turbofan data)

| # | File | Topic |
|---|------|-------|
| 06 | [`06-python-ml-example-predictive-maintenance.txt`](transcripts/06-python-ml-example-predictive-maintenance.txt) | Predictive maintenance in Jupyter: remaining useful life, a "fails within 30 cycles" label, feature selection by correlation, `MinMaxScaler`, logistic regression, random forest, a PyTorch neural network |

### Live practical

| # | File | Topic |
|---|------|-------|
| 07 | [`07-week-9-live-practical-genai-data-and-assignment-2-help.txt`](transcripts/07-week-9-live-practical-genai-data-and-assignment-2-help.txt) ([`.srt`](transcripts/07-week-9-live-practical-genai-data-and-assignment-2-help.srt)) | Locating public datasets and generating synthetic data with Copilot; Assignment 2 help: plots, data wrangling, evidence, dataset versions, correlation, regression, Sections 4–5 |

## Data

| File | What it is |
|------|------------|
| [`data/train_FD001.txt`](data/train_FD001.txt) | NASA C-MAPSS FD001 training set: 20,631 rows covering 100 engines, each run until it fails. The file is space-delimited with no header. Its 26 columns are engine ID, cycle, 3 operational settings and 21 sensors. |
| [`data/test_FD001.txt`](data/test_FD001.txt) | FD001 test set: 13,096 rows covering 100 engines. Each run stops at some point *before* the engine fails. It has the same 26 columns. |

## Source file mapping

The uploaded files were renamed by topic. `transcript.txt` (unnumbered) was a byte-identical copy of transcript 1 and is stored once. The live practical came as subtitles; the original `.srt` is kept alongside a plain-text version with the timestamps removed.

| Stored as | Original upload |
|-----------|-----------------|
| 01 | transcript 1 and the unnumbered transcript (identical) |
| 02 | transcript 2 |
| 03 | transcript 3 |
| 04 | transcript 4 |
| 05 | transcript 5 |
| 06 | transcript 6 |
| 07 | `EGH404_26Sem2_Week_9_Practical.srt` |
| `slides/dealing-with-unpredictability-uncertainty.pdf` | `EGH404_Uncertainty.pdf` |
| `slides/week-9-practical-genai-data-generation-and-assignment-2-help.pdf` | `week_9.pdf` |
| `data/train_FD001.txt`, `data/test_FD001.txt` | `train_FD001.txt`, `test_FD001.txt` |

**Not included:** the Canvas practical page also links a sample prompt, `prompt for data generation.docx`. It wasn't in the upload. The notes reconstruct its structure from the practical recording.
