# Beyond the Wildcards: An Empirical Study of Semantic Templates for Security Event Logs with Large Language Models
## by Despoina Giarimpampa, Olumuyiwa O. Ojo, Iyiola E. Olatunji, Tegawendé F. Bissyandé, and Jacques Klein

This repository contains additional details and information to support the reproducibility of the stated results.

## Overview of the STeLLM - Named Template Detection pipeline.

<img width="1428" height="723" alt="System Design" src="https://github.com/user-attachments/assets/5cb46864-097f-43a1-8cdc-12569a6a1f33" />

## Code Execution

STeLLM's goal is to examine whether existing unsupervised, in-context learning based template detection pipelines can be extended to produce semantically meaningful templates through representation and prompt design alone, under otherwise unchanged conditions. 

STeLLM, an unsupervised LLM-based named template detection system inspired by the design principles of LLM-TD.

To execute the code, follow the procedure provided [here](https://github.com/ristov/llm-td/).

However, depending on the experiment, selecting either the generic prompt or the targeted prompt correctly from the Prompts folder is crucial to obtaining the expected result. 

## Datasets
We evaluate STeLLM on a set of popular and publicly-available real-world security event log datasets released by [Vaarandi and Bahşi](https://github.com/ristov/llm-td/tree/main/logs)
