# teach-ChatGPT-your-R-library
Fine tune ChatGPT on your R functions!

A good practice of R programming is to document all the functions using a `roxygen2`-like flavour, commenting them using the `#'` chars before the definition. For example:

```R
#' This is an example of how to document functions
#' @param function_name character. Name of the function we are documenting now
#' @param function_usage character. description of the function
#' @outputs description of how to use the function
function_example <- function(function_name, function_usage){
  description <- paste0(function_name, ' is a function that is used for ', function_usage)
  return(description)
}
```

In big projects, many of this utility functions can be created, and eventually be grouped in a library.

In this repo I fine tuned ChatGPT over a set of functions having that standard format, to 'teach' to the model the work I've done so far and leverage on its help in the future. 

## Prerequisites

- An OpenAI API key is required to use this program. Visit https://beta.openai.com/signup/ to sign up for an API key if you don't have one already
- Python 3.6 or later installed on your system
- A conda virtual environment

To install anaconda on your IOS system follow the guide at [Medium](https://medium.com/ayuth/install-anaconda-on-macos-with-homebrew-c94437d63a37).
Once it is installed, create the conda virtual env and activate it running:
```bash
conda create --name myenv
conda activate myenv
```


Install the openai Python package by running:
```bash
conda install -c conda-forge openai
```

## Setup

- Clone the repository or download the it (running `git clone https://github.com/ferrazzipietro/teach-ChatGPT-your-R-library.git`)
- Modify the a `CONFIG.json` file in the root directory of the project adding your information, included you API KEY
- Copy your `.R` file containing the functions in the `roxygen2` format. Make sure that each function has its comment section and that the file contains only the functions of interest and nothing else. 


## Usage

- Open a terminal/command prompt and navigate to the directory containing the source code.
- Fine tune the choosen model running:
  ```bash
  python main.py
  ```
  The idea is that the comments to the function are given to the model has they were the prompts, while the function itself is the completion.
- if the queue of Openai is crowded, you might recive a message saying `run openai api fine_tunes.follow -i YOUR-SESSION-CODE to relaunch the session`. If it happens, make sure to add your openai API KEY:
  ```bash
  openai -k YOUR-API-KEY api fine_tunes.follow -i YOUR-SESSION-CODE
  ```

## Costs

The cost of the fine tuning depends on the model. Now (18/06/2023) the available ones are the following:

<img width="838" alt="image" src="https://github.com/ferrazzipietro/teach-ChatGPT-your-R-library/assets/92532181/f410bfa3-133f-4975-9854-3abcfaddaef9">

the prices can be find at the 'Fine tuning models' section of [OpenAi Pricing](https://openai.com/pricing).

For me, the fine tuning of `davinci` costed around 4$ for 100 imputed functions, while ada costed me 0.05$ for the same amount of input data.



## Acknowledgements

 - [OpenAI](https://github.com/openai/openai-python)
 - [ChatGPT](https://openai.com/blog/chatgpt)
 - [abroniewski](https://github.com/abroniewski/CoverLetter-Generator.git)

![Logo](https://i.imgur.com/BBhcHDx.gif)


