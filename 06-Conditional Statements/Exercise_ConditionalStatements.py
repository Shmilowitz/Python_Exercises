import random
#Exercise 1
print('\n')
adj = ["other", "new", "good", "high", "old", "great", "big", "American",
    "small", "large", "national", "young", "different", "black", "long", 
    "little", "important", "political", "bad", "white", "real", "best", 
    "right", "social", "only", "public", "sure", "low", "early", "able", 
    "human", "local", "late", "hard", "major", "better", "economic", 
    "strong", "possible", "whole", "free", "military", "true", "federal", 
    "international", "full", "special", "easy", "clear", "recent", 
    "certain", "personal", "open", "red", "difficult", "available", 
    "likely", "short", "single", "medical", "current", "wrong", "private", 
    "past", "foreign", "fine", "common", "poor", "natural", "significant", 
    "similar", "hot", "dead", "central", "happy", "serious", "ready", 
    "simple", "left", "physical", "general", "environmental", "financial", 
    "blue", "democratic", "dark", "various", "entire", "close", "legal", 
    "religious", "cold", "final", "main", "green", "nice", "huge", 
    "popular", "traditional", "cultural"] 

articles = ["the", "a", "an"] 

nouns = ["time", "year", "people", "way", "day", "man", "thing", "woman",
    "life", "child", "world", "school", "state", "family", "student", 
    "group", "country", "problem", "hand", "part", "place", "case", 
    "week", "company", "system", "program", "question", "work", 
    "government", "number", "night", "point", "home", "water", "room", 
    "mother", "area", "money", "story", "fact", "month", "lot", "right", 
    "study", "book", "eye", "job", "word", "business", "issue", "side", 
    "kind", "head", "house", "service", "friend", "father", "power", 
    "hour", "game", "line", "end", "member", "law", "car", "city", 
    "community", "name", "president", "team", "minute", "idea", "kid", 
    "body", "information", "back", "parent", "face", "others", "level", 
    "office", "door", "health", "person", "art", "war", "history", 
    "party", "result", "change", "morning", "reason", "research", "girl", 
    "guy", "moment", "air", "teacher", "force", "education"] 

verbs = [ "say", "go",  "get",  "make", "know", "think", "take", "see", "come", "want", 
    "look", "use", "find", "give", "tell", "work", "may", 
    "call", "try", "ask", "need", "feel", "become", "leave", "put", 
    "mean", "keep", "let", "begin", "seem", "help", "talk", "turn", 
    "start", "might", "show", "hear", "play", "run", "move", "like", 
    "live", "believe", "hold", "bring", "happen", "must", "write", 
    "provide", "sit", "stand", "lose", "pay", "meet", "include", 
    "continue", "set", "learn", "change", "lead", "understand", "watch", 
    "follow", "stop", "create", "speak", "read", "allow", "add", "spend", 
    "grow", "open", "walk", "win", "offer", "remember", "love", 
    "consider", "appear", "buy", "wait", "serve", "die", "send", "expect", 
    "build", "stay", "fall", "cut", "reach", "kill", "remain"]
#"be", "have", "do", "can", "would", "will", "could", "should", 
vowels = ('a','e','i','o','u')

cons = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z")
	
for i in range(11):
	rArt = random.choice(articles)
	rNoun = random.choice(nouns)
	rVerb = random.choice(verbs)
	
	if (rArt == "a"):
		if(rNoun.startswith(vowels)):
			rArt = "an"
	if (rArt == "an"):
		if(rNoun.startswith(cons)):
			rArt = "a"
	if(rVerb.endswith("y") and rVerb[-2] == "l"):
		rVerb = rVerb[:-1]
		rVerb += 'ies'
	else:
		rVerb += 's'
	print(rArt, rNoun,rVerb)
	