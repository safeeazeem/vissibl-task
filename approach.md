
# Approach

This was not a RAG Task, because we were not retrieving anything specific in this task. This was more of a form filling task, where we had an input(The Questionnaire) and the output format(ISO DOCUMENT). A RAG would have been useful here if we had to answer some sort of question, and due to the limited context window, we would extract similar chunks(Retrieve), format them with prompt(Augment) and then use an LLM to get an answer(Generation).

I also had to fix a section typo in the ISO format because, the table of content and the sections were numbered wrong. 

I used OPENAI GPT4.1 Model here which is a new model and is great at following instructions. It comes with enhanced context window size and also can generate up to 16k tokens at once, which is useful for longer generations. I also went ahead with this model because its needle in the haystack accuracy is over 90% from 10k context size up to 1M. Another reason I went with this model is because it is trained on larger context data. We have the same usecase to, where we are giving the questionnaire, template, then the content is read from the questionnaire and then the template is generated with the new information.

I went ahead a wrote a custom Agent Class, that is reusable, The reason I did that was because It gives me more control over what I want to achieve.  We can add more agents here. This is present in `agents/agents.py`.

I used two agents here.
  
    1. Editor Agent
    2. Validator Agent

### Editor Agent  
The Editor Agent was responsible for preparing the ISO template using the questionnaire. Nowadays LLM's have advanced quite a lot and with extended context window, we are able to add much more context into it. Due to that, I was able to add in the entire questionnaire, and the ISO Template in the prompt. The content generated is customized to the company in the provided sections. However, there is a mention of `Customized content sections`, I think what this means is generating customizable section headings, that is something I experimented with, but all it was doing was giving me a separate section fro `Company Profile` at the end.  


I have left the final document as a text file but its in a markdown format with all the tags, that was on purpose because we can later convert that same markdown to a PDF. You can check that in `./output/alec_engineering_2025-04-20_21:12:01_c8b14af9_output.txt`


### Validator Agent
The Validator Agent was responsible for checking if there is anything missing and would generate a report that is saved in the PDF format. The reason I added this was because it can also help us identify the missing values and sections that require additional support from the company. The Validator Agent works because it has the questionnaire, the ISO Template and the prepared ISO Template by the Editor Agent, using these 3 sources, validation is possible.

The agent outputs a Table, which identifies Issues section by section. This is only possible after converting the ISO template into a markdown. It also generates a summary at the end. You can check that in `./output/alec_engineering_2025-04-20_21:12:01_c8b14af9_validation_output_report.pdf`


# How can this be further improved?
This can be further improved by generating the template section by section, what I mean by that is that we can split the ISO template into different sections. We can then send `n` number of parallel requests and populate each section, and then combine them at the end. This will be useful if we have a template which is very long.

### Bonus: Customized content sections based on company profile​

To Improve this, I think having some examples of ISO documents can help the model include and discard sections, because we only have one template and often times we will only have one, the model tries its best to follow that.



