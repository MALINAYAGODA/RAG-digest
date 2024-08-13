from langchain_community.llms.ollama import Ollama

prompt = """
Answer the question based only on the following context:

MONOPOLY 
Property Trading Game from Parker Brothers" 
AGES 8+ 
2 to 8 Players 
Contents: Gameboard, 3 dice, tokens, 32 houses, I2 hotels, Chance
and Community Chest cards, Title Deed cards, play money and a Banker's tray.
Now there's a faster way to play MONOPOLY. Choose to play by
the classic rules for buying, renting and selling properties or use the
Speed Die to get into the action faster. If you've never played the classic
MONOPOLY game, refer to the Classic Rules beginning on the next page.
If you already know how to play and want to use the Speed Die, just
read the section below for the additional Speed Die rules.
SPEED DIE RULES
Learnins how to Play with the S~eed Die IS as
/
fast as playing with i't.
1. When starting the game, hand out an extra $1,000 to each player

---

1. When starting the game, hand out an extra $1,000 to each player
(two $5005 should work). The game moves fast and you'll need
the extra cash to buy and build.
2. Do not use the Speed Die until you've landed on or passed over
GO for the first time. Once you collect that first $200 salary, you'll
use the Speed Die for the rest of the game. This means that some
players will start using the die before others.
3. Once you start using the Speed Die, roll it along with the two
white dice on your turn. Then do the following depending on
what you rolled.
1, 2, or 3: Add this number to the roll of the two white
dice. You'll zoom around the board.

---

Each player is given $1,500 divided as follows: P each of $500s,
$100~ and $50~; 6 $40~; 5 each of $105, $5~ and $Is.
All remaining money and other equipment go to the Bank. Stack the ..
Bank's money on edge in the compartments in the plastic Banker's tray.
BANKER. Select as Banker a player who will also
make a good Auctioneer A Banker who plays
~n the game must keep hislher personal funds
separate from those of the Bank. When more than
f~ve persons play, the Banker may elect to act only
as Banker and Auctioneer.
THE BANK: Besides the Bank's money, the Bank
holds the Title Deed cards and houses and hotels prior to purchase
and use by the players. The Bank pays salaries and bonuses. It sells
and auctions properties and hands out the~r proper Title Deed cards;

---

CLASSIC MONOPOW RULES
OBJECT: The object of the game IS to become the
wealthiest player through buying, renting and selling
property.
PREPARATION: Place the board on a table and put
the Chance and Community Chest cards facedown on
their allotted spaces on the board. Each player chooses one token to
represent himther while traveling around the board.

---

and auctions properties and hands out the~r proper Title Deed cards;
it sells houses and hotels to the players and loans money when
required on mortgages.
The Bank collects all taxes, fines, loans and interest, and the price of
all properties which it sells and auctions.
The Bank nwer "goes broke." If the Bank runs out of money, the Banker
may issue as much more as needed by writing on any ordinary paper.
THE PLAY: Starting with the Banker, each player in turn throws the dice.
The player with the highest total starts the play: Place your
token on the corner marked "GO," throw the dice and move
your token in the direction of the arrow the number of
spaces indicated by the dice. After you have completed
your play, the turn passes to the left. The tokens remain

---

Answer the question based on the above context: How much total money does a player start with in Monopoly? (Answer with the number only)"""
model = Ollama(model="mistral")
print('model_start')
response_text = model.invoke(prompt)
print('model_end')
print(response_text)