# Week 9 Study Notes – Machine Learning, Generative AI and Uncertainty

These notes summarise the Week 9 transcripts in [`transcripts/`](transcripts/) and the slides in [`slides/`](slides/). Transcript numbers in brackets, such as (06), point to the matching file.

**Dataset:** NASA C-MAPSS turbofan engine degradation data, subset FD001 ([`data/`](data/)). It is used in the Python machine learning example (06).

**How the numbers were checked:**
- The FD001 figures below were recomputed with pandas and scikit-learn.
- The probability examples were recomputed by hand.
- Where a figure differs from what the lecturer said, the notes say so.

**Assignment link:** the practical (07) covers **Assignment 2, Sections 4 and 5**: locating or synthesising preliminary data, then analysing its correlation. It also gives tips for Sections 1–3, and it explains how this work feeds into the **Assignment 3** research pitch.

---

## 1. What machine learning is (01, 02)

### Definition
- Machine learning (ML) is a subfield of artificial intelligence. It lets a machine **learn from past data without being explicitly programmed**.
- **Programming vs ML:**
  - In programming, you have data and you write a program that produces the output.
  - In ML, you have the data *and* the desired output, and the computer works out the "program" (the model). You then reuse that model on new data.
- **Two phases:**
  - **Training:** the model learns patterns from examples. The examples can be tabular data, images, video or speech.
  - **Testing:** the model is given data it has **never seen** during training, to check how well it learned.
- **Applications:**
  - robotics and self-driving cars;
  - security surveillance (detecting unusual behaviour);
  - social networks ("people you may know");
  - biology and healthcare (detecting abnormalities such as gene mutations);
  - finance (automated trading, fraud detection).

### Why engineers should care (02)
- Many engineering analysis and prediction tools have an ML component "under the hood".
- If you put your name to a decision that came from such a tool, you need to understand how it works and what its pitfalls are.
- Software and electrical engineers may end up building these tools.

### Statistics vs data mining vs machine learning (02)

| | What it does | Predicts? |
|---|---|---|
| **Statistics** | Describes the data: min, max, central tendency, spread, distribution, correlation | Not really; it describes |
| **Data mining** | Finds patterns and information in very large datasets, for example visualisation, clustering and anomaly detection | No; it finds what is already in the data |
| **Machine learning** | Learns rules or decision functions from a **training set**, so it can act on or predict from new data | Yes; it extrapolates from the data |

- ML relies heavily on statistics in the background but goes a step further than description.
- Data mining is broad and searches for information. ML focuses on performing a (human) task.

---

## 2. Types of learning (01, 03)

### The three paradigms

| Paradigm | Labels? | Idea | Examples |
|---|---|---|---|
| **Supervised** | Yes | Learn the mapping from inputs to known labels | Regression (salary from years of experience; cyclist counts from weather), classification (dog vs bird images) |
| **Unsupervised** | No | Find patterns or groupings in the data on its own | Clustering, dimensionality reduction |
| **Reinforcement** | Rewards and penalties | An **agent** learns behaviour through rewards and penalties, much like training a dog | OpenAI's hide-and-seek agents, robotics |

- Reinforcement learning is **not used further** in this unit, because it mostly applies to robots and intelligent agents.

### Discrete vs continuous (03)

| | Discrete | Continuous |
|---|---|---|
| **Supervised** | Classification or categorisation | Regression |
| **Unsupervised** | Clustering | Dimensionality reduction |

### Supervised learning in detail (03)
- Use supervised learning when **you know the answer** for every training example (the label or ground truth).
- Regression fits a line. A classifier finds a line, plane or **hyperplane** (a decision boundary) that separates the classes.
- **Overfitting:**
  - A very wiggly boundary can separate the training set almost perfectly and still do poorly on the test set.
  - A simpler, straight boundary makes a few more training errors but **generalises better**.
  - The complex model has learned the *noise* in the training set; it is "over-parameterised".
  - The goal is **not** the highest possible training accuracy. It is the best accuracy you can get **without overfitting**.

### Unsupervised learning in detail (03)
- Use unsupervised learning when there are no labels, either because you can't get them or because they don't matter.
- **Clustering:** group similar points, for example by x–y location.
  - Algorithms: **k-means** (covered later in the semester), **Gaussian mixture models (GMMs)** and agglomerative clustering. All are available in MATLAB.
  - Real-world examples: sorting images into ballet vs yoga, and **image segmentation** (grouping pixels by position and colour into sky, cloud, grass and so on).
- **Dimensionality reduction:**
  - It simplifies a dataset with many variables. It can select useful variables, extract a smaller feature set, or project the data into a more discriminative space.
  - Methods: **PCA** (principal component analysis) and **LDA** (linear discriminant analysis).
  - PCA appears as an option in MATLAB's Classification and Regression Learner apps. It is **not examined** in this unit.

### The traditional ML pipeline (01)
1. **Feature extraction:** convert the data into numbers and remove redundancy. Features are characteristics that describe the data, for example a cat's whiskers and claws.
   - Traditional features are hand-designed with expert knowledge.
   - Modern deep learning models learn features automatically.
2. **Model:** the features go into a model, which learns to perform the task.
- CNNs (convolutional neural networks) can act as both the feature extractor and the classifier.

---

## 3. Data for machine learning (04)

### Garbage in, garbage out
- If the input data is poor, the model will be poor, however clever the algorithm.
- Andrej Karpathy's point: **academia focuses on the model, industry focuses on the data**. Better or more data usually gets you most of the way.
- The data must be **fit for purpose**:
  - **Coverage:** include enough examples of every condition you want to model. For bike counts, that means enough weekdays *and* weekends, and every weather condition.
  - **Accurate ground truth:** if the labels (for example the cyclist counts) or the inputs (for example the weather variables) are noisy, the model learns the noise. Know about noise in advance so you can compensate for it or fix it.

### Training, validation and test sets

| Set | Used for |
|---|---|
| **Training** | Fitting the model's **parameters**, for example regression slopes and intercepts |
| **Validation** | Choosing **hyperparameters**: the model type (linear or quadratic), which terms to include, and so on. It detects overfitting, because an overfitted model does badly here. |
| **Test** | A **completely unseen** final check that mimics deployment in the real world |

- All three sets should have **similar statistical properties** (means, standard deviations and so on).
- Some fields swap the names "validation" and "test". This unit uses the definitions in the table.

### Not enough data?
- **k-fold cross-validation:**
  - Split the training data into, say, **5 folds**, which gives an **80/20 split** each time.
  - Train on 4 folds and validate on the 5th, then rotate so that every fold is the validation set once.
  - Average the performance across the folds. This is the same cross-validation used in the Regression Learner app in Week 8.
- **ML might not be appropriate.** With only a dozen or two data points, the data may not contain the pattern at all, and extrapolating beyond the data is risky.

### The curse of dimensionality
- Using every available variable is tempting, but with many dimensions and few samples the feature space becomes **sparse**, and the model overfits.
- Keep only the informative variables. Use correlation with the response, as in Weeks 7 and 8, or PCA/LDA.
- **Rule of thumb:** each extra variable roughly **doubles** the data you need. This varies by algorithm.
- **Keep models as simple as you can.**

---

## 4. Neural networks and deep learning (01, 05)

### Biological vs artificial neurons

| Biological | Artificial |
|---|---|
| Dendrites carry electrical impulses into the cell | Inputs x₁, x₂, … |
| The cell body's chemistry transforms the signal | Weighted sum Σ wᵢxᵢ, then an activation function |
| The axon transmits the output | Output yᵢ |
| **Synapses** (gaps between neurons) strengthen or weaken with experience | **Weights** on the connections, learned during training (the "trainable parameters") |

- A weight controls how much each input contributes. A small weight on x₁ means x₁ contributes little.
- Neural networks date back to the **1940s**. They only took off once GPUs provided enough computing power.

### Network structure
- **Input layer → hidden layer(s) → output layer.**
- A network with **one** hidden layer is a **shallow** network. **Two or more** hidden layers make a **deep** neural network (DNN).
- Each layer transforms the output of the layer before, so stacking layers gives progressively more refined features.

### Representation learning (01, 05)
- A DNN learns its own features from the raw data. For images, the inputs are **pixel values**.
- On a face image, for example:
  - the **early layers** learn edges and contours;
  - the **middle layers** learn parts, such as a nose or eyes;
  - the **final layers** learn the whole object, such as the face.

### How a network is trained (05)
1. Collect a labelled **training set**, for example thousands of animal images from the internet.
2. Shuffle the set and pass examples through the network, which produces a prediction.
3. Compute the **loss** (how wrong the prediction is), work out each weight's contribution to the error, and **adjust the weights**.
4. One pass through the whole training set is one **epoch**. Repeat for many epochs until performance stops improving.
5. Evaluate on a separate, unseen **test set** to measure accuracy.

Face recognition and voice recognition on your phone are trained this way.

---

## 5. Generative AI (01, 05)

### What it is
- Generative AI (GenAI) is a collection of ML tools that **create new content**: text, images, audio, code and video. It is **not just text**.
- **Language modelling:**
  - Predict the next word ("Once upon a time there… *was*"). Google Autocomplete is an everyday example.
  - The model learns how human language works from huge amounts of text.
- **Examples:** text-to-image ("a robot horse in a museum"), and ArchitectGPT (sketch to realistic floor plan or image).

### Milestones (05)

| Year | Milestone |
|---|---|
| 2014 | **GANs** (generative adversarial networks) |
| 2015 | **Attention** models |
| 2017 | **Transformers**, which are built on attention |
| Recent | GPT-4, which can process spreadsheets and generate graphs; Sora (text to video) |

- **GPT** stands for **Generative Pre-trained Transformer**.
- **Attention** means weighting the earlier words differently when predicting the next word, for example focusing more on "there" than on "once".

### How ChatGPT is trained (01, 05)
The lecturers describe this as reinforcement learning from human feedback (RLHF):
1. **Supervised fine-tuning:** collect sample prompts with human-written answers, for example "Explain the moon landing to a six-year-old", and train the model on them.
2. **Reward (ranking) model:** the model generates several answers to a prompt, and humans **rank** them by relevance. An answer about lunar gravity may be correct but is less suitable for a six-year-old. A second network learns to reproduce these rankings.
3. **Reinforcement learning:** the generator produces answers, the reward model scores them, and the scores are used as rewards and penalties to update the generator.

### Other GenAI examples (01, 05)
- **Sora (OpenAI):**
  - Text to realistic video, for example "historical footage of California during the gold rush". The footage is convincing but **fake**.
  - At the time of the lecture it had not been publicly released.
- **Deepfakes:**
  - Digitally altered video that makes one person appear to be someone else.
  - Used in film, for example the younger Will Smith in *Gemini Man*.
- **Adversarial attacks:**
  - A second network learns to fool the first. Examples are special eyeglasses that make face recognition identify someone else, or patches on a **stop sign** that make an autonomous car misread it.
  - They work because deep models learn redundant features. **Deep learning models are not perfect.**

### Engineering applications (05)

| Discipline | Tool | Use |
|---|---|---|
| Civil | **Nerfstudio** (NeRF, neural radiance fields) | Stitch photos into an editable 3D model of a site; simulate floods, fire and similar events on the structure |
| Civil/architecture | **Midjourney** | Text-to-image sketching and blending, for example concept images for reports |
| Mechanical | **Autodesk Fusion 360** generative design | Set parameters for a part, generate candidate designs, run simulations, pick one and swap it into the assembly |
| Electrical/software | **GitHub Copilot** | Code generation, trained specifically on GitHub's code |

### Risks and limitations (01, 05)
- **Training data can be wrong:** internet text, even Wikipedia, isn't always accurate.
- **Bias:** racial, political and other biases in the training data carry through to the outputs.
- **Hallucination:** when asked about something it hasn't seen, the model still produces a confident answer. **Fact-check everything.**
- **Realistic fakes:** synthesised content can look entirely real.

### Academic integrity (05)
- **Do not submit GenAI-generated answers** for assignments unless the unit coordinator has explicitly allowed it. It is the same as copying a friend's answer.
- If you can't **explain and defend** your answer, that is an academic integrity breach and possibly contract cheating. The penalty mentioned is exclusion for a semester, with every unit that semester failed.
- In your **professional career**, where it is permitted, GenAI can boost your productivity.
- **Assignment 2 exception:** Section 4B explicitly allows GenAI to generate synthetic data (see section 8).

---

## 6. Python ML example: predictive maintenance (06)

### The task
- Predict whether an **aircraft engine will fail within the next 30 cycles** from its current sensor readings. This is a **binary classification** problem.
- Predictive maintenance means planning maintenance before a critical failure happens.
- The data is NASA's prognostics data repository, C-MAPSS FD001, in [`data/`](data/). It runs in Jupyter; see the Week 7 Python setup instructions.

### The data
- Space-delimited with no header. The columns are `engine_id`, `cycle`, `op_setting_1–3` and sensors 1–21.
- The lecturer says "23 sensors" because each line ends with trailing spaces. pandas reads those as two extra all-NaN columns (sensors 22 and 23), which are then dropped with `dropna(axis=1)`.
- The **same columns must be dropped from the test set** so that the two sets have the same format.
- Each engine runs from cycle 1 until it fails. In the training data:
  - engine 1 has **192 cycles**;
  - engine 2 has **287 cycles**.

### Building the label
1. **Remaining useful life (RUL)** = the engine's maximum cycle − the current cycle.
   - Compute each engine's maximum with `groupby('engine_id')['cycle'].max()`, `merge` it back on `engine_id`, and subtract.
   - Check: engine 1's first row has RUL = 192 − 1 = **191**, and engine 2's first row has RUL = 287 − 1 = 286. The lecturer said 285, which is off by one.
2. **Label:** `failure_within_30 = np.where(RUL < 30, 1, 0)`.

### Feature selection by correlation
- Correlate each column with the label and keep the strongly correlated ones.
- These are the recomputed correlations on the training data:

| Sensors | Correlation with "fails within 30" |
|---|---|
| s11 | +0.66 |
| s4 | +0.64 |
| s15 | +0.62 |
| s17, s2 | +0.58 |
| s3 | +0.56 |
| s8 | +0.54 |
| s13 | +0.54 |
| s9 | +0.42 |
| s14 | +0.34 |
| s20 | −0.60 |
| s21 | −0.60 |
| s7 | −0.62 |
| s12 | −0.64 |

- Sensors s1, s5, s10, s16, s18, s19 and `op_setting_3` are **constant** in FD001, so they have no correlation at all.
- The lecture used **16 features**; the exact list isn't read out. The inputs are called `X` and the label `y`.

### Pre-processing
- `MinMaxScaler` rescales every feature to [0, 1]; [−1, 1] is also fine. Models handle large raw values poorly.
- **Fit the scaler on the training data only**, then apply it to the test data.
- The shapes are 16 features × 20,631 training rows and 16 features × 13,096 test rows.

### Models and results

| Model | Key settings | Test accuracy in the lecture | Recomputed |
|---|---|---|---|
| **Logistic regression** (`sklearn.linear_model.LogisticRegression`) | defaults | **79.6%** | about 78.7–78.8% |
| **Random forest** (`RandomForestClassifier`) | 15 trees (`n_estimators=15`) | about **78%** | about 78.9% |
| **Neural network** (PyTorch) | 16 → 50 → 12 → 2, ReLU, cross-entropy loss, Adam optimiser, 300 epochs | **78.1%** | not rerun |

- **About the recomputed column:**
  - The lecture's exact feature list and random seed aren't known, so the reruns used the sensors in the correlation table, with and without two extra columns.
  - Every variant scored 78.7–78.9% for both models, which is close to the lecture's figures.
- **Logistic regression** is the classification counterpart of linear regression. Its output is a class, not a continuous value.
  - For one example test engine, which the lecturer describes as failing at about cycle 200, it starts predicting "fail" confidently at about cycle 180.
- **Random forest:**
  - Many decision trees, each trained on a **random subset of features**, vote, and the majority wins.
  - `feature_importances_` shows which inputs the model relies on. **s11** is the most important, which the recomputation confirms at about 0.24–0.30, followed by s4.
  - Suggested exercise: vary `n_estimators` and `random_state`.
- **The PyTorch network:**
  - Convert the data to tensors: features become `float` and labels `long`.
  - Define the layers in `__init__` and the forward pass in `forward`, with ReLU for non-linearity.
  - Each epoch runs a forward pass, computes the loss, runs `backward()`, then calls `optimizer.step()`.
  - Plot the loss curve to decide when to stop. In the lecture it flattens out at about 150–250 epochs.
  - The network outputs two class probabilities, so take the `argmax` to get the prediction.
  - For the example engine it gave weak predictions and flagged failure only late (the transcript says "around 109", which is probably a mis-transcribed 190). This suggests poor generalisation. Diagnosing underfitting or overfitting is beyond the scope of the unit.
- Other optimisers mentioned: SGD and RMSprop.

### Caveats (not raised in the lecture)
- **Always compare against a baseline.**
  - Only 22.9% of test rows are labelled "fail within 30", so a model that **always predicts "no failure" scores 77.1%**.
  - The models' ~79% is only slightly better than that. Look at per-class results, such as a confusion matrix or recall on the "fail" class, not just accuracy.
- **The test labels aren't true failures.**
  - The FD001 test engines stop *before* failure. The notebook computes test RUL from each engine's last *recorded* cycle, as if that cycle were the failure.
  - NASA supplies the true test RUL in a separate file (`RUL_FD001.txt`), which wasn't provided.
  - So the test accuracy measures agreement with an approximate label.
- The classes are imbalanced: 14.5% of training rows are "fail within 30", compared with 22.9% of test rows.

---

## 7. Dealing with unpredictability (Uncertainty slides)

This deck has no matching transcript.

### Why randomness?
- Research tries to understand the world from **incomplete information**. We may not know what to measure, we may be unable to measure it, or we may not have the resources to measure everything.
- Incomplete information introduces uncertainty, which we model as randomness.

### The three ingredients of a probability model
1. **Sample space Ω:** the set of possible outcomes.
   - One coin toss: {H, T}. Two tosses: {HH, HT, TH, TT}.
   - Grades: {1, …, 7}.
   - Thumb length: (0, ∞). Thumb and index finger lengths: (0, ∞)².
2. **Events:** subsets of Ω.
   - For two tosses: "first toss is heads" = {HH, HT}; "no tails" = {HH}; "tosses differ" = {HT, TH}.
   - For grades: "you pass" = {4, 5, 6, 7}.
   - For lengths: "thumb in (50, 60] mm and index in (80, 90] mm".
3. **Probability function P:**
   - P(A) ≥ 0 for every event, and P(Ω) = 1.
   - For **disjoint** events, P(A₁ or A₂ or …) = P(A₁) + P(A₂) + ….
   - It can be discrete or continuous.

### Independence and how it misleads
- A and B are **independent** if one outcome has no effect on the other. Then **P(A and B) = P(A)·P(B)**.
- **The Sally Clark case (Goldacre, *Bad Science*, chapter 14):**
  - Two of Sally Clark's babies died. The prosecution assumed the two SIDS deaths were independent, so the chance was (1/8500)², about **1 in 73 million**.
  - That was wrong. Families who lose a first child to SIDS have about a **1 in 100** chance of losing the second the same way, due to shared genetic and environmental factors.
  - The slide puts the real incidence of double SIDS at about **1 in 130,000**. Sally Clark was wrongly convicted.
- **The Monty Hall problem:**
  - There are three doors: a car behind one, goats behind the others. You pick door 1. The host, who knows where the car is, opens door 3 to show a goat and offers door 2.
  - **You should switch.** Your first pick wins with probability 1/3, and switching wins with probability 2/3.
  - The host's choice is *not* independent of where the car is. Many professors and PhDs confidently got this wrong when Marilyn vos Savant published it.
- **In engineering:**
  - Independence is often assumed, for example that failure modes in reliability analysis are independent.
  - **Be critical.** Common-cause failures break the assumption.

### Conditional probability and base-rate neglect
- **P(A | B) = P(A and B) / P(B)**, provided P(B) > 0.
- **The damage test example:**
  - 1% of components are damaged: P(D+) = 0.01.
  - The test detects damage 80% of the time: P(T+ | D+) = 0.80.
  - It gives a false positive 9.6% of the time: P(T+ | D−) = 0.096.
  - What is P(D+ | T+)?

  P(D+ | T+) = (0.8 × 0.01) / (0.8 × 0.01 + 0.096 × 0.99) = 0.008 / 0.10304 ≈ **0.078, or 7.8%**

- Most people guess 60–100%. Because damage is **rare**, false positives (9.5% of all components) far outnumber true positives (0.8%). This is **base-rate neglect**.
- The deck ends with an area-proportional Euler diagram by Luana Micallef, using a medical diagnosis example.
- **Takeaway:** always consider the base rate. A "good" test for a rare event produces mostly false alarms.

---

## 8. Week 9 practical: GenAI for data, and Assignment 2 help (07, practical slides)

### Practical objectives (Canvas page 9.4)
- Explore GenAI for creating **synthetic data**, and **critically evaluate** what it produces: reliability, validity and ethics.
- Learn how GenAI can simulate datasets when real data is limited or sensitive.
- **Preparation:** review the Week 9 modules and bring your Assignment 2 draft.
- The Canvas page provides the slides (`week_9.pdf`) and a sample prompt (`prompt for data generation.docx`, not in this folder).

### How the assignments link up
- **Assignment 1:** choose a topic, review the literature, set research questions.
- **Assignment 2:** data analysis. Its **last two sections** (4 and 5) link to Assignment 1 by using data related to *your* research topic.
- **Assignment 3** (research project pitch presentation): section 6, "Evaluation methods and reflection using preliminary data", presents initial evaluations based on the Assignment 2 preliminary data. It also discusses that data's limitations and challenges.
  - The idea is to pitch to a panel of academic and industry experts, using the preliminary analysis as supporting evidence.

### Option A (preferred): locating a public dataset with GenAI
- Real data shows **real-world correlations**, so the analysis makes more sense.
- **Example prompt** (in Microsoft Copilot): "I need help locating publicly available data on the topic of *evaluating the structural performance of recycled concrete*. Provide me with data descriptions and the URLs. The data should be strictly tabular…"
  - Replace the topic with your own.
  - Constraints such as "strictly tabular" help the model check its own results, which reduces hallucinated links.
- **Results in the demo:** natural-fibre and recycled-aggregate concrete datasets on Mendeley Data. **Open the links and check that the dataset really exists.**
- **If your topic isn't tabular** (for example image segmentation of heart images), find a *related* tabular dataset instead, such as heart rate or ECG sensor measurements.

### Option B (last resort): generating synthetic data
- **Main limitation:** you can constrain each column (its range and distribution), but the **relationships between columns** that come from domain knowledge and the literature won't appear unless you specify them.
  - For example, the literature may show that a concrete additive increases durability. Randomly generated data won't show that correlation.
  - If this happens, discuss it in your interpretation.
- **Prompt structure** (reconstructed from the demo; the full prompt is on Canvas):
  1. **Role:** "You are a data generator." Giving the model a role often improves the results.
  2. **Output only:** "Create a synthetic dataset in CSV, no prose, no Markdown tables, no code fences." This stops it giving you code to run instead of data.
  3. **Row count:** about **200 rows**. You need roughly 100–200 rows for meaningful analysis.
  4. **Schema:** define every column. The demo used renewable energy plants: plant ID, plant name, country, region, energy source, capacity (MW), commission date, operator ID and name, generation, CO₂ savings.
  5. **Relationships and constraints:**
     - IDs are unique, and each operator ID maps one-to-one to an operator name.
     - The energy source comes from a fixed set.
     - Capacity ranges depend on the energy source (solar, wind, hydro). **Take the ranges from the literature** for your topic.
     - Dates follow a fixed format (probably ISO; the transcript garbles it), and each region matches its country.
     - Watch for impossible combinations, such as a 20-year-old with 30 years' experience. Add explicit cross-column constraints to prevent them.
  6. **Realism and consistency:** no duplicate rows, realistic names, and fixed ID formats such as P001.
  7. **Output format:** CSV only, a single header row, about 200 rows, comma-separated, no explanation.
  8. **Validation rules at the end:** many models check their own output against them.
  9. "Return the CSV."
- **Check the output:**
  - Line breaks between rows may be missing; ask the model to regenerate with them.
  - Open the file in Excel and check that every value makes sense, including fixing date formats.
- **For Assignment 2, use the same research topic as Assignment 1**, so that the variables and ranges come from your literature review.

### Assignment 2 tips (practical slides and 07)

**Plots (1 mark or 0):**
- Every plot needs a **title, axis titles, consistent axis labels, and a legend** if applicable.
- A plot missing any of these gets **zero**.

**Section 1: data wrangling (1.1.C and 1.2.C):**
- List each problematic data point (outliers, missing data, errors) with its date, the handling method, and a **justification**.
- **Don't just write "removed outliers".** Explain *why* the method suits *this* data. For imputation, explain why you chose the mean, median or mode.
  - **Imputation example:** temperatures differ between seasons, so impute a winter gap with the *seasonal* mean, not the annual mean.
  - **Outlier example:** a QUT Open Day spike is a real event. You might remove it for typical-usage analysis but keep it for resource planning.
- Report **up to 3 examples per problem type** (outliers, missing data, errors) **for each bikeway** (Bicentennial and North Brisbane). If there are fewer than three, report all of them.
  - There is no need to split pedestrians and cyclists.
  - A run of consecutive missing days handled the same way can be reported as a date range, but not as one enormous range.
- **Interesting cases:**
  - An outlier does not automatically mean removal. First check whether it is explainable.
  - Use **line plots** as well as box plots to see patterns.
  - Look for sensor faults, for example the same reading for several days, or days that break the trend.
  - If one sensor drops while a correlated one rises, it is probably a real event, not a fault.
  - Search online for events such as floods or bikeway and bridge closures, then decide.

**Supporting evidence (appendix):**
- **MATLAB or Python:** paste the code, or export the live script or notebook to PDF and merge it with your document.
- **Excel:** screenshots of the formulas and the Data Analysis tool dialogs.
  - One screenshot per repeated process is enough, for example one box plot setup and then the final plots.

**Use the correct dataset version:**
- **Section 1** uses the **raw** datasets. **Sections 2 and 3** use the **clean** versions provided, *not* your own cleaned data. This keeps marking consistent.
- The provided clean version is not "the answer" to Section 1, so don't try to reverse-engineer it.

**Section 2: correlation:**
- **S2.T1:** report the command used and the correlation values.
- **S2.T3** (400 words) should cover:
  - general observations: what clusters you see;
  - explanations or hypotheses: seasonal variation, demographics, preferences;
  - what the coefficient implies.
- **Clusters distort Pearson r**, because every point is compared with the overall mean.
  - The slides show clusters that each trend *positively* while the overall r = **−0.35**.
  - Split by a grouping variable (for example weekday vs weekend) and correlate each group separately.

**Section 3: multiple linear regression:**
- **Build one model with all the identified independent variables**, not separate two-variable models.
  - Repeat the fit, removing variables, until every remaining variable is statistically significant.
- **Train/test split:**
  - Split by the date ranges given in the assignment. The train period ends on **31 December 2017**, inclusive, and the rest is test data. Using other dates changes your answers.
  - The recording garbles the start date as "January 1, 2024". The supplied data runs from 2014 to 2018 (see [`../assignment-2/README.md`](../assignment-2/README.md)), so the split is almost certainly **1 Jan 2014 – 31 Dec 2017 for training and 2018 for testing**. Confirm on the assignment page.
- **Report:**
  - the regression summary table from the **training** data;
  - **RMSE on both the training and test sets**, compared and discussed;
  - scatter plots of the **training** data.
- **Section 3.2 interpretation** (400 words):
  - What do the **F-statistic, R² and p-values** say about the model?
  - Use the plots to describe how well the model captures the trends.
  - Give a rigorous interpretation, not just a list of numbers.

**Section 4: locating or synthesising preliminary data:**
- **4A:** a public dataset (preferred). **4B:** synthetic data, as a last resort.
- Use your **Assignment 1 topic**.

**Section 5: correlation analysis using the preliminary data:**
- Analyse and interpret the correlations.
- If the data is synthetic and lacks the expected correlations, discuss why.

---

## Key takeaways

1. **ML learns the program from data and known outputs.** Supervised learning needs labels; unsupervised learning finds structure without them.
2. **Avoid overfitting.** The goal is generalisation to unseen data, not training accuracy. Keep the validation and test sets separate, and use cross-validation when data is scarce.
3. **Data matters more than the algorithm.** Garbage in, garbage out. Make sure the data covers every condition and has accurate labels, and beware the curse of dimensionality.
4. **Deep learning** stacks layers of weighted neurons that learn features automatically, trained by minimising a loss over many epochs.
5. **GenAI is powerful but fallible.** It hallucinates, inherits bias and makes convincing fakes. Fact-check it, and don't submit it as your own work.
6. **Always compare accuracy with a baseline.** In the FD001 example, predicting "no failure" every time already scores 77%.
7. **Question independence assumptions**, as the Sally Clark case and the Monty Hall problem show, and **don't neglect base rates**: a positive test for a rare event is probably a false alarm.
8. **For Assignment 2:**
   - Plots need all their labels.
   - Justify every data-handling choice.
   - Use the clean datasets for Sections 2 and 3.
   - Build one regression model and report RMSE on both splits.
   - Prefer real public data for Section 4.
