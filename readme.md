Normalization of Russian for TTS
================================

Inspired by [this Kaggle competition](https://www.kaggle.com/c/text-normalization-challenge-russian-language).

Work in progress text normalization system for Russian. Text normalization is the process by which text is rewritten
into some single consistent form. This can include anything from changing "$30" to "thirty dollars" to removing diacritics
for simpler storage in a database. In this case, the idea is to format text to feed into a text to speech (TTS) program.

Normalizing English for TTS already has its share of difficulties. To steal Wikipedia's example, "vi" could be a numeral, the 
name of the text editor, or short for the name "Violet." Russian futher complicates things with its case system, particularly
when it comes to numbers and dates.

For example, the text "2010" with no other contextual information could be normalized as две тысячи десять (dve tisyachi desyat'). 
But a user of a TTS system might actually have the year in mind, which would be normalized as две тысячи десятый (год). With more context
we can more confidently identify what exactly that "2010" is meant to be, but the normalized form has to make grammatical sense.
с 2010 года would become с две тысячи десятого года (s dve tisyachi desyatovo goda), while без 2010 долларов would become 
без двух тысяч десяти долларов (bez dvukh tisyach desyati dollarov). That's a big difference in how the number needs to be said.

The basic idea here is to use rules where they're easy enough to write and attempt to figure out the rest from the Kaggle training
data. Unfortunately the Kaggle data has some grammatical errors, but we'll have to work with what we've got. Manual correction may be an option.

Additional features that will likely be useful are part of speech tags that include grammatical information such as
case and gender and word context (bigrams, trigrams, etc).