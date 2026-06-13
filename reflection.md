# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  1. There is no regulation for input, even though the input can be given between 1 to 100.
  2. Incorrect hint message: If the secret number chosen is lower, still the hint given is to choose a higher number
  3. Incorrect scoring after guessing the right number. Negative number is being given as score

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 120   |  Error                 No error
| 64    |  Lower (if no. <64)   Go Higher!
|       |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
I used claude code and asked it what kind of corrections are to be expected and in which section for the same. However, claude did suggest me to make some corrections in app.py which were unneccessary, so I decided to reject those recommendations
## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I ran the file and checked whether the edge cases were being passed or not.
I gave the input as -1 as mentioned above to check whether an error message is being given in the game or not.
I tried making the test cases by myself as I choice quite generic bugs or ones which were quite obvious in the code
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
When any change is made in the code, the entire python application is run from top to bottom. This is called rerunning. Session state basically allows variables to be run during the rerunning process in streamlit rather than creating them from scratch again.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I would definitely use llms wisely and check everytime something is suggested, cause some suggestions may be unneccessary or may even damage the original code.
Next time I would try to find more errors or errors which are not so obvious. 
This project allowed me to play around with streamlit as well. At the same time, I learnt how to spot errors, whether code recommended is correct or not and how to check what a function truly has to say.