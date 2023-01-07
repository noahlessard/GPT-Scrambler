# GPT-Scrambler
 A space to organize techniques to evade programs meant to detect AI generated text.

AI detection is going to become a necessity in the future, and current applications just aren't good enough. Here are some easy ways to fool them. However, these detection techniques will probably evolve over time, so best not to submit this to anything you really care about! I take no responsibility for any mischievous behaviour, I just think this is a good way to get the word out about these flaws.

(For these tests, I used https://openai-openai-detector.hf.space/ and http://gltr.io/dist/index.html. They seem to be the most accurate and widely used tools to detect AI text).

While tools like https://quillbot.com/ and other rephrasing techniques work, there is an even easier way! By adding in random invisible unicode characters, you can get very "real" results without having to change the text at all!

This script let me try this out and see these results. If you want to play around with it yourself, you can run it with

```
python main.py -i *path to text file*
```

and it will give an output in its folder with the scrambled text.

### Text before scrambling in a generic detector
![alt text](https://github.com/noahlessard/GPT-Scrambler/blob/main/before_scramble.PNG)

### Text after scrambling in a generic detector
![alt text](https://github.com/noahlessard/GPT-Scrambler/blob/main/so_real_its_fake..PNG)


### Before scrambling in a detailed detector
![alt text](https://github.com/noahlessard/GPT-Scrambler/blob/main/before_scramble_detailed.PNG)


### After scrambling in a detailed detector
![alt text](https://github.com/noahlessard/GPT-Scrambler/blob/main/characters%20dont%20show%20in%20detailed%20scan.PNG)
