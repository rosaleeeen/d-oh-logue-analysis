# D'OH-LOGUE ANALYSIS: CODE BOOK

this codebook is designed to assign **one primary topical category** to the following minor characters in The Simpsons: Ned Flanders, C. Montgomery Burns, Seymour Skinner.

---

## 1. CODING FRAMEWORK

### 1.1 general decision process

for line in char_lines:
1. **read the whole line once** (no coding yet).  
2. ask:  
   > **"What is this line ultimately about? What is its main subject or point?"**  
3. identify all **candidate topics** that appear (REL, FAM, WRK, ECO, COM, CON, PER, LEI).  
4. choose the topic that best describes **the main point** of the line (given the below rules).  
5. assign the topic code.

### 1.4 context & tie-breaker rules

- if a line mentions multiple topics:
  - code the topic that is **argued for**, **evaluated**, or **treated as the goal** of the line.
- if a line is still difficult to place:
  - use the **character's core themes** as a helper:

    - **Ned Flanders**: REL > FAM > COM  
    - **Seymour Skinner**: WRK > CON > FAM  
    - **C. Montgomery Burns**: ECO > WRK > CON > LEI  


---

## 2. TOPIC SUMMARY

### 2.1 top-level topic defn

| code | topic | what is the line mainly about? |
|------|-------|--------------------------------|
| REL  | religion, scripture, moral worldview | God, Bible, church, sin, salvation, moral rules, divine will, big "right vs wrong" |
| FAM  | family, marriage, close/intimate relationships | spouses, children, parents, kin, household life, romance, breakups |
| WRK  | work, school, institutional authority | nuclear plant, school, bosses, employees, rules, duties, bureaucracies |
| ECO  | money, business, wealth, material resources | money, profit, wealth, costs, budgets, deals, ownership, financial risk |
| COM  | community, neighbours, society, groups             | neighbours, citizens, Springfield, crowds, voters, public opinion, social reputation, demographics |
| CON  | conflict, crime, risk, war, punishment | violence, war, crime, threats, sanctions, danger, security |
| PER  | self, identity, inner life | speaker's own feelings, guilt, pride, self-image, inner doubts, self-description |
| LEI  | leisure, culture, music, everyday pastimes | songs, TV, films, games, sports, trips, parties, food, casual fun |


---

## 3. DETAILED TOPIC DEFINITION

### 3.1 REL – RELIGION, SCRIPTURE & MORAL WORLDVIEW

**def:**  
lines whose main point is about **religion**, **the Bible**, **God**, **faith**, or a **moral worldview** framed as right/wrong, virtue/vice, or divine will.

**diagnostic qs:**
- is the character talking about **God, the Lord, Jesus, the Bible, church, or prayer**?
- is the line fundamentally a **moral judgment** ("right thing", "sinful", "wicked")?
- is the line alluding to the **Bible**?

**inclusions:**
- line quotes or explains **Scripture** / **biblical book**:
  - "thus ends the book of Malachi…"
  - any recognizable verse-like sentence that is clearly framed as Bible (if unsure, complete a quick Google search!).
- discussion of **God, Lord, Jesus, faith, salvation, sin, heaven, hell, the devil**.
- moralising lines where the main content is **ethical evaluation**:
  - that's wrong in the eyes of the Lord."
- "power" framed as **divine power**, *power of prayer*, or God's power.

**exclusions:**
- line mentions "church" only as a place where people are (social, not theological) → **COM**.
- line is mainly about **money**, **work**, or **politics**, with only a throwaway "God" exclamation → code by actual domain (**ECO/WRK/COM**).
- character is simply expressing **personal guilt or shame** without religious framing → **PER**.

**helpful character cues:**
- **Ned Flanders**:  
  - direct prayers, quoting verses, invoking God's will.  
  - lines explaining why something is sinful or Christian.
- **Burns & Skinner**:  
  - ironic moral sermons, where moral ideals are the main subject.

---

### 3.2 FAM – FAMILY, MARRIAGE, CLOSE/INTIMATE RELATIONSHIPS

**defn:**  
lines whose main point is **family relationships** (spouse, children, parents, kin) or **romantic relationships**.

**diagnostic qs:**
- is the line about **a spouse, partner, children, parents, or close kin** (regardless of whether they are alive)?
- is the line about **marriage, divorce, dating, heartbreak, or family responsibilities**?

**inclusions:**
- dicussions of:
  - **wife, husband, mother, father, son, daughter, kids, children, family**.
  - **marriage, divorce, engagement, heartbreak**.
  - **domestic life**: raising kids, household struggles, family traditions.

**exclusions:**
- character mentions "mother" or "my boys" as a throwaway reference, but the main point lies within another domain.
  - Skinner recalling "Mother's preserves" as part of a Vietnam story → **CON** (not **FAM**).
- family words used metaphorically for organizations:
  - "we're one big family at the plant" → **WRK**.
- lines of **romantic power or money** (e.g., marrying for money) → **ECO** if wealth is central.

**helpful character cues:**
- **Ned**: Maude, Rod, Todd, his "boys," being a widower.
- **Skinner**: "Mother" lines that focus on his relationship, dependence, or conflict with her.
- **Burns**: Occasional references to long-lost fiancees or family scandals.

---

### 3.3 WRK – WORK, SCHOOL, INSTITUTIONAL AUTHORITY

**defn**  
lines primarily about **jobs**, **institutions**, **hierarchy**, **roles**, **rules**, and **duties** (especially nuclear plant and Springfield Elementary).

**diagnostic qs:**
- is the line about **how the plant/school works**, rules, staff, duties, or bureaucratic decisions? 
- is this about the character acting in their **official role** (boss, principal, employee)?

**inclusions:**
- plant-related:
  - "Nuclear plant", "reactor", "Sector 7G", "safety inspector", "employee", "firing staff", "union trouble".
- school-related:
  - "Springfield Elementary", "principal", "teachers", "students", "test scores", "detention", "PTA".
- dicussion of **work roles, promotions, performance, inspections**.
- "power" that clearly comes from a **formal role or position**:
  - Burns: "i have the power to fire everyone in this plant." → **WRK**.
  - Skinner: "as principal, I have the power to expel you." → **WRK**.

**exclusions:**
- discussions of:
  - **money/profit** rather than tasks or roles → **ECO**.
  - **violence or threat** at work → **CON**.
  - coworkers as a social group ("everyone at the plant loves me") and the content is reputation → **COM**.

**helpful character cues:**
- **Skinner**: assemblies, discipline speeches, class rules, school announcements.
- **Burns**: staff meetings, plant policies, threats to fire or reward employees.
- **Ned**: his store, Leftorium, as a place of work (when the line is about running the business, not money).

---

### 3.4 ECO – MONEY, BUSINESS, WEALTH, MATERIAL RESOURCES

**defn**  
lines whose main focus is **money**, **wealth**, **profit**, **cost**, **financial risk**, or **ownership of material resources**.

**diagnostic qs:**
- is the line mainly about **how much something costs**, or **gaining/losing money or wealth**?
- is "power" clearly tied to **being rich, owning things, or controlling assets**?

**inclusions:**
- discussions of:
  - **dollars, profits, wages, budget, stock, shares, investments, fortunes, millions**.
  - **business schemes**, **tontines**, **inheritance**, **deals**, **bets** framed as financial risk.
- boasting or lamenting about **being rich or poor**.
- "power" explicitly tied to wealth:
  - "i have wealth and power beyond your dreams" → **ECO**.

**exclusions:**
- line is mainly about **plant/school structure or roles** → **WRK**.
- line is primarily about **punishment or crime** (e.g., stealing nuclear weapons as crime) → **CON**.
- line is about "power of faith/God" → **REL**.

**helpful character cues:**
- **Burns** (very frequent): fortune, stocks, buying/selling, "richest man in Springfield", expensive schemes.
- **Skinner**: school budgets, funding crises.
- **Ned**: store profits, financial troubles at the Leftorium.

---

### 3.5 COM – COMMUNITY, NEIGHBOURS, SOCIETY, GROUPS

**defn**  
lines whose main subject is **other people as a group**, the **community**, **neighborhood**, **social reputation**, or **analysis of society**.

**diagnostic qs:**
- is the line about **Springfield**, **citizens**, **neighbours**, or **crowds**?
- is the focus on what **"people" think, do, or how they behave together**?

**inclusions:**
- dicussions of:
  - **Springfield**, **citizens**, **the town**, **our community**, "the people".
  - **neighbours** and **neighborhood disputes**:
    - Ned vs. Homer as neighbours, fences, noise, yard behaviour.
  - **crowds, voters, audiences**, **churchgoers** as a social group.
- Reputation in community:
  - "what will people say?", "the whole town will see me as…"

**exclusions:**
- dicussions of:
  - **town safety or riots** where danger and violence are central → **CON**.
  - **specific family members** rather than "people in general" → **FAM**.
  - **employees** mainly in terms of workplace rules → **WRK**.

**helpful character cues:**
- **Ned**: references to neighbours, the neighbourhood's behaviour, what Springfield thinks.
- **Burns**: speeches to "citizens of Springfield", talk about voters and public opinion.
- **Skinner**: talk about parents, PTA, or the school community as a social body.

---

### 3.6 CON – CONFLICT, CRIME, RISK, WAR, PUNISHMENT

**defn**  
lines whose main subject is **conflict**, **violence**, **war**, **crime**, **threats**, **punishment**, or **danger**.

**diagnostic qs:**
- is the line basically about **threatening, harming, punishing, or being in danger**?
- is the line a **war story**, a **crime plot**, or a **punishment scenario**?

**inclusions:**
- war and combat: **Vietnam**, "‘Nam", **battle**, **enemy**, **foxhole**, **bombs**, **grenades**.
- crime and punishment: **crime**, **stealing**, **arrest**, **jail**, **prison**, **sentence**, **execution**.
- active threats:
  - "release the hounds."
  - "i'll destroy this town."
  - "if you cross me, you'll pay dearly."
- "power" defined as ability to **hurt, punish, or destroy**:
  - Burns boasting he can destroy Springfield with one button → **CON**.

**exclusions:**
- line is about **power from wealth** (not threat) → **ECO**.
- line is about **discipline as school rules** without real sense of danger → **WRK**.
- line is about **moral evil or sin** in an abstract sense → **REL**.

**helpful character cues:**
- **Skinner**: Vietnam flashbacks, war trauma, prisoner-of-war stories.
- **Burns**: threats to release hounds, steal nuclear weapons, crush competitors or the town.

---

### 3.7 PER – SELF, IDENTITY, INNER LIFE

**defn**  
lines whose main subject is **the character's own inner state, feelings, self-image, or personal transformation**.

**diagnostic qs:**

- is the character primarily talking about **how they feel**, **what kind of person they are**, or **how they see themselves**?
- is the line mostly **self-evaluation**, **guilt**, **pride**, **shame**, or **doubt**?

**inclusions:**
- explicit feeling talk:
  - "i feel…", "i'm afraid…", "i'm ashamed…", "i regret…", "i'm proud…".
- identity talk:
  - "i'm not a bad man."
  - "i've never been happier to be Seymour Skinner."
  - "deep down, i'm a coward."
- self-focused doubt or crises:
  - Ned questioning whether he has failed God and his family **if the main focus is his own failing** (not doctrine).
- "power" as **inner empowerment**:
  - "for the first time i feel i have the power to change myself."

**exclusions:**
- line is a moral self-assessment centered on divine judgment → **REL**.
- line is about **role identity** as principal, boss, etc., with emphasis on the role responsibilities → **WRK**.
- line is about sympathy or judgment toward **others**, not self → **COM/REL** depending on moral framing.

**helpful character cues:**
- **Ned**: guilt, doubt, whether he's a good Christian, self-reproach.
- **Skinner**: insecurities about being a strict/repressed principal.
- **Burns**: changes of heart, doubt about his own success, rare moments of introspection.

---

### 3.8 LEI – LEISURE, CULTURE, MUSIC, EVERYDAY PASTIMES

**defn**  
lines mainly about **entertainment, songs, culture, games, trips, food, or everyday casual activities**.

**diagnostic qs:**

- is the line essentially about **a song, performance, movie, TV, sports, party, vacation, everyday enjoyment, or some creative endeavour**?
- is the main point to **describe or perform entertainment**?

**inclusions:**
- musical numbers:
  - Burns' songs or other verses/singing.
- cultural references and media:
  - TV shows, movies, film references, shows at the school.
- games, sports, fun events:
  - betting as **fun**, casino outings, picnics, parties, carnivals.
- food and casual treats when central:
  - e.g., donuts, cakes, ice cream, barbecues.

**exclusions:**
- bet or game is primarily about **financial risk and profit** → **ECO**.
- school play is used to talk about **discipline or rules** → **WRK**.
- leisure event is used as a context for **crime or tragedy** → **CON** when danger/punishment is central.

**helpful character cues:**
- **Burns**: especially musical sequences, vanity performances, showy spectacles, elaborate bets framed as entertainment.
- **Skinner**: school shows, talent nights, cultural field trips where the main point is the event, not the institution.
- **Ned**: church camp songs, family outings, picnics, when not obviously tied to doctrine (otherwise **REL**).

---

## 4. HANDLING MIXED-TOPIC LINES

sentences that can fit into multiple topics should be handled as followed:

### 4.1 stepwise decision

1. **identity all clear topics mentioned** (REL/FAM/WRK/ECO/COM/CON/PER/LEI).
2. ask:
   > **"if i had to summarize this line in one clause, what would i say it is about?"**
3. choose the topic that is:
   - **evaluated**, **argued for**, or **treated as the goal** of the line.

### 4.2 Examples

- **Burns**:  
  "family, religion, friendship – these are the three demons you must slay if you wish to succeed in business."  
  - mentions REL and FAM, but the point is success in **business** → **ECO**.

- **Ned**:  
  "Lord, I tried to be a good father, but this town mocks me and I feel I've failed You."  
  - REL, FAM, COM, PER all appear.  
  - if the line is framed as a prayer about failing God → **REL**.  
  - if framed more as a confession about himself → **PER**.  
  - choose based on what seems to be the line's **ultimate focus**.

- **Skinner**:  
  "if we don't raise test scores, the school loses funding and i lose my job."  
  - school, test scores, funding, his job → all WRK/ECO.  
  - the central concern is the fate of the school and his role → **WRK**.

---

## 5. SPECIAL DISTINCTION: "POWER"

when **"power"** appears, classify it by **type of power**, using this table:

| kind of "power" described                                        | tag         |
|------------------------------------------------------------------|------------:|
| power from **wealth, owning things, elite status**               | **ECO**     |
| power from a **role** (boss, principal, owner, authority figure) | **WRK**     |
| power to **harm, threaten, destroy, wage war**                   | **CON**     |
| power of **God, faith, prayer, miracles**                        | **REL**     |
| power as **inner strength or personal empowerment**              | **PER**     |