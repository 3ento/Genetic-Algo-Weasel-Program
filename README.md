<h1>The Weasel Program</h1>

<blockquote>
I don't know who it was first pointed out that, given enough time, a monkey bashing away at random on a typewriter could produce all the works of Shakespeare. The operative phrase is, of course, given enough time. Let us limit the task facing our monkey somewhat. Suppose that he has to produce, not the complete works of Shakespeare but just the short sentence 'Methinks it is like a weasel', and we shall make it relatively easy by giving him a typewriter with a restricted keyboard, one with just the 26 (capital) letters, and a space bar. How long will he take to write this one little sentence?
<br><br>
The sentence has 28 characters in it, so let us assume that the monkey has a series of discrete 'tries', each consisting of 28 bashes at the keyboard. If he types the phrase correctly, that is the end of the experiment. If not, we allow him another 'try' of 28 characters. I don't know any monkeys, but fortunately my 11-month old daughter is an experienced randomizing device, and she proved only too eager to step into
the role of monkey typist.
</blockquote>

> ...

<blockquote>
So much for single-step selection of random variation. What about cumulative selection; how much more effective should this be? Very very much more effective, perhaps more so than we at first realize, although it is almost obvious when we reflect further. We again use our computer monkey, but with a crucial difference in its program. It again begins by choosing a random sequence of 28 letters, just as before.
<br><br>
It now 'breeds from' this random phrase. It duplicates it repeatedly, but with a certain chance of random error 'mutation' in the copying. The computer examines the mutant nonsense phrases, the 'progeny' of the original phrase, and chooses the one which, however slightly, most resembles the target phrase.
</blockquote>
This is a simple genetic algorithm, implementing Richard Dawkins' thought experiment. A key difference from the original is a drastically decreased mutation rate (one much more akin to real life, but still on the higher end).
