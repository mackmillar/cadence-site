# Content for the cadencegym.app guides. Rendered by build.py.
# Voice: docs/tone-of-voice.md — plain, British, no exclamation marks, no guilt, no hype.

# The one-line definition. Keep it word for word wherever Cadence is described
# (home FAQ, JSON-LD, llms.txt, press page, App Store), so AI tools can repeat it.
DEFINITION = ("Cadence is a gym habit app for iPhone that notices when you arrive at your gym "
              "and counts the visit automatically. No workout logging.")

CTA = ('<div class="callout"><p><strong>How Cadence helps.</strong> ' + DEFINITION + ' You set a weekly target '
       'and the days you mean to go, and your streak is counted in weeks, with one missed week a month forgiven '
       'automatically.</p></div>'
       '\n  <a class="cta" href="./">See how Cadence works</a>')

GUIDES = [
{
 "slug": "how-often-should-you-go-to-the-gym",
 "title": "How often should you go to the gym? A weekly gym schedule you can keep",
 "short": "How often should you go to the gym?",
 "h1": "How often should you go to the gym?",
 "kicker": "A weekly gym schedule you can keep",
 "desc": "How many times a week to go to the gym, whether twice a week is enough, what the NHS guidance says, and simple two, three and four-day gym schedules.",
 "card": "Two, three or four days, and how to pick the number you’ll keep.",
 "published": "2026-10-29", "modified": "2026-10-30",
 "body": """
  <p><strong>Short answer: two or three times a week is enough for most people, and the right number is the one you can keep in a busy week.</strong> A modest plan you hit every week does more than an ambitious one you abandon in February.</p>

  <h2>What the guidance says</h2>
  <p>The <a href="https://www.nhs.uk/live-well/exercise/physical-activity-guidelines-for-adults-aged-19-to-64/" rel="noopener">NHS physical activity guidelines</a> for adults ask for two things each week:</p>
  <ul>
    <li>Strengthening activities that work all the major muscle groups on at least two days.</li>
    <li>At least 150 minutes of moderate activity, or 75 minutes of vigorous activity, spread across the week.</li>
  </ul>
  <p>Two gym sessions a week covers the first. Walking, cycling to work or a third session covers the second. Nothing in the guidance asks for five days a week.</p>

  <h2>Is going to the gym twice a week enough?</h2>
  <p>Yes, for most goals. Twice a week meets the strength guidance on its own, and two full-body sessions are enough to get stronger and build muscle, especially in your first year. It’s also the easiest number to keep, which matters more than anything else on this page.</p>
  <p>Add a third day when two feels routine, not before. The people who go twice a week for a year end up well ahead of the people who went five times a week for a month.</p>

  <h2>Pick your number by your worst week, not your best</h2>
  <p>Most people set a target from their most motivated moment, usually a Monday in January. Then a late meeting, a cold or a weekend away knocks out a session, the week counts as a failure, and the habit goes with it.</p>
  <p>Set the target from an ordinary, slightly-too-busy week instead. If you think you could manage four, plan three. Going more than you planned feels good. Going less than you planned feels like a fail, even when you still went twice.</p>

  <h2>Simple weekly gym schedules</h2>
  <p>These are schedules for <em>when</em> to go, not what to do once you’re there. Any sensible full-body or split programme fits inside them.</p>

  <h3>Two days a week</h3>
  <div class="tablewrap"><table><thead><tr><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th><th>Sun</th></tr></thead><tbody><tr><td>Gym</td><td>–</td><td>–</td><td>Gym</td><td>–</td><td>–</td><td>–</td></tr></tbody></table></div>
  <p>Good for a first habit, or a demanding job. Leave two or three days between sessions so a missed day can slide without wrecking the week.</p>

  <h3>A 3-day gym routine</h3>
  <div class="tablewrap"><table><thead><tr><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th><th>Sun</th></tr></thead><tbody><tr><td>Gym</td><td>–</td><td>Gym</td><td>–</td><td>Gym</td><td>–</td><td>–</td></tr></tbody></table></div>
  <p>The classic. A rest day between each session, and the weekend free as a back-up if one slips. Three full-body sessions, or a push, pull and legs rotation, both fit.</p>

  <h3>Four days a week</h3>
  <div class="tablewrap"><table><thead><tr><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th><th>Sun</th></tr></thead><tbody><tr><td>Gym</td><td>Gym</td><td>–</td><td>Gym</td><td>–</td><td>Gym</td><td>–</td></tr></tbody></table></div>
  <p>For people who already go regularly and want more. Usually paired with an upper/lower split so back-to-back days work different muscles. See <a href="how-many-rest-days-a-week">how many rest days you need</a> before going higher.</p>

  <h2>Make the days specific</h2>
  <p>“Three times a week” is easy to postpone until it’s Friday. “Monday, Wednesday, Friday, after work” isn’t. Decide the days and a rough time once, so you’re not deciding every morning. If you’re not sure when, here’s <a href="best-time-to-go-to-the-gym">how to pick the best time to go</a>.</p>
  <p>Keep one day as a spare. If Wednesday goes wrong, Saturday picks it up and the week still counts.</p>

  <h2>Count weeks, not days</h2>
  <p>A daily streak breaks on the first rest day, which is the day you’re supposed to rest. Counting weeks fixes that: the question is just “did I hit my number this week?” One bad week then costs one week, not the whole streak.</p>
""",
 "faq": [
  ("How many times a week should I go to the gym?", "Two or three times a week is enough for most people. It meets the NHS guidance of strength exercise on at least two days a week. Pick the number you can keep in a busy week."),
  ("Is going to the gym twice a week enough?", "Yes, for most goals. Twice a week meets the strength guidance, and two full-body sessions are enough to get stronger and build muscle, especially in your first year."),
  ("Is it OK to go to the gym every day?", "It can be, if you vary what you train and keep the intensity sensible, but most people don't need to. One or two rest days a week gives muscles time to recover and makes the habit easier to keep."),
 ],
 "related": ["how-many-rest-days-a-week", "best-time-to-go-to-the-gym", "how-long-does-it-take-to-form-a-habit"],
},
{
 "slug": "how-long-does-it-take-to-form-a-habit",
 "title": "How long does it take to form a habit? What the research says about the gym",
 "short": "How long does it take to form a habit?",
 "h1": "How long does it take to form a habit?",
 "kicker": "What the research says, and what it means for the gym",
 "desc": "Not 21 days. The best-known study puts the median at 66 days, and exercise habits take longer than most. What that means for building a gym habit that lasts.",
 "card": "Not 21 days. What the research actually found, and why the gym takes longer.",
 "published": "2026-10-30",
 "body": """
  <p><strong>Short answer: about two months on average, with a very wide range, and exercise tends to sit at the slow end.</strong> The “21 days” figure you’ve probably heard isn’t from a study of habits at all.</p>

  <h2>Where “21 days” came from</h2>
  <p>The number traces back to a 1960 self-help book by a plastic surgeon, Maxwell Maltz, who noticed patients took “a minimum of about 21 days” to get used to a change in their appearance. Over the years “a minimum of about” fell away, and it became a rule it was never meant to be.</p>

  <h2>What the research found</h2>
  <p>The study most people cite is <a href="https://onlinelibrary.wiley.com/doi/10.1002/ejsp.674" rel="noopener">Lally and colleagues at UCL (2009)</a>. They asked 96 people to pick a daily behaviour and repeat it in the same situation for 12 weeks, rating each day how automatic it felt.</p>
  <ul>
    <li>The median time to reach a plateau of automaticity was <strong>66 days</strong>.</li>
    <li>The range ran from <strong>18 to 254 days</strong>, depending on the person and the behaviour.</li>
    <li>Exercise habits took longer to become automatic than simpler ones, like drinking a glass of water with lunch.</li>
    <li>Missing a single day didn’t meaningfully set people back.</li>
  </ul>
  <p>A later study using check-in data from tens of thousands of gym members reached a similar conclusion: going to the gym takes months, not weeks, to become habitual.</p>

  <h2>What that means if you’re trying to make the gym a habit</h2>
  <h3>Expect it to feel effortful for a while</h3>
  <p>If week three still takes willpower, nothing has gone wrong. That’s the normal part of the curve. Most people quit around here because they assume it should be easy by now.</p>

  <h3>A missed session doesn’t reset the clock</h3>
  <p>The UCL finding that one missed day didn’t matter is the most useful line in the paper. Habits are built by the overall pattern, not an unbroken chain. Treat a missed session as weather, not a verdict.</p>

  <h3>Keep the cue the same</h3>
  <p>Habits form around a context: the same days, roughly the same time, the same gym. “Monday, Wednesday, Friday after work” becomes automatic far faster than “three times a week, whenever”. If you’re still choosing, read <a href="how-often-should-you-go-to-the-gym">how often to go</a> and <a href="best-time-to-go-to-the-gym">when to go</a>.</p>

  <h3>Make the bar low enough to clear on a bad day</h3>
  <p>Turning up is the habit. A short session on a tired evening still repeats the cue and the routine. See <a href="how-long-should-a-gym-session-be">how long a session needs to be</a>.</p>

  <h3>Count weeks, not days</h3>
  <p>A daily streak breaks on your first rest day. A weekly one asks a fairer question: did you hit your number this week? That keeps the pattern visible through the slow middle months, which is exactly when it’s needed.</p>
""",
 "faq": [
  ("How long does it take to form a habit?", "In the best-known study, from UCL, the median was 66 days, with a range from 18 to 254 days depending on the person and the behaviour. The popular 21-day figure isn't based on habit research."),
  ("How long does it take to make going to the gym a habit?", "Usually months rather than weeks. Exercise habits take longer to become automatic than simpler daily habits, so expect it to feel effortful for the first couple of months."),
  ("Does missing a day break a habit?", "No. In the UCL study, missing a single day didn't meaningfully affect how automatic the habit became. The overall pattern matters more than an unbroken streak."),
 ],
 "related": ["how-often-should-you-go-to-the-gym", "gym-anxiety", "how-long-to-see-results-from-the-gym"],
},
{
 "slug": "best-time-to-go-to-the-gym",
 "title": "The best time to go to the gym (and when it’s quietest)",
 "short": "The best time to go to the gym",
 "h1": "What’s the best time to go to the gym?",
 "kicker": "Morning, lunch or evening, and when it’s quietest",
 "desc": "Morning or evening? The research on timing, when gyms are busiest and quietest, and why the best time to go to the gym is the one you can repeat every week.",
 "card": "Morning or evening, the quiet hours, and why the answer is mostly about you.",
 "published": "2026-10-30",
 "body": """
  <p><strong>Short answer: the best time is the one you can repeat every week.</strong> The physical differences between morning and evening training are small. The difference between a time that fits your life and one that doesn’t is enormous.</p>

  <h2>Does the time of day affect results?</h2>
  <p>A little. Some studies find strength and power are slightly higher in the late afternoon and early evening, when body temperature peaks. People who train consistently at one time also seem to adapt to it, so morning regulars perform well in the morning.</p>
  <p>Those effects are small next to the one that matters: whether you actually go. A perfectly timed session you skip does nothing.</p>

  <h2>Morning, lunch or evening</h2>
  <h3>Morning</h3>
  <p>Hardest to start, easiest to keep. Nothing has had a chance to go wrong yet, so meetings, plans and tiredness can’t crowd it out. Gyms are usually calm before about 7am. The cost is the alarm, and a warm-up that needs a bit longer.</p>

  <h3>Lunchtime</h3>
  <p>Good if your gym is close to work and your lunch break is real. Sessions tend to be shorter and focused, which suits a lot of people. It’s the first slot to disappear in a busy week, so give it a back-up day.</p>

  <h3>Evening</h3>
  <p>Where most people go, which is both its strength and its weakness. You’re warmed up and often a little stronger, but you’re also tired, and plans have all day to get in the way. Weekday evenings between about 5pm and 8pm are the busiest hours in most gyms.</p>

  <h2>When is the gym quietest?</h2>
  <p>Every gym is different, but the pattern is reliable:</p>
  <ul>
    <li><strong>Quietest:</strong> mid-morning (roughly 9am to 11am), early afternoon on weekdays, and the last hour or two before closing.</li>
    <li><strong>Busiest:</strong> weekday evenings from about 5pm to 8pm, and early weekday mornings in gyms near offices.</li>
    <li><strong>By day:</strong> Monday and Tuesday are usually the busiest days, and Friday evening and Sunday afternoon the quietest.</li>
    <li><strong>By month:</strong> January is the busiest month of the year and calms down by February.</li>
  </ul>
  <p>Many gym apps show live occupancy, and Google Maps shows a “popular times” chart for most gyms. A quieter slot helps a lot if crowds put you off; see <a href="gym-anxiety">gym anxiety</a>.</p>

  <h2>How to choose</h2>
  <p>Look at an ordinary week and find the slot that survives it. Then pick days as well as a time, so the decision is made once, not every morning. <a href="how-often-should-you-go-to-the-gym">How often to go</a> covers the days.</p>
  <p>Consistency of time also helps the habit form: the same cue at the same point in the day becomes automatic faster. More on that in <a href="how-long-does-it-take-to-form-a-habit">how long a habit takes</a>.</p>
""",
 "faq": [
  ("What is the best time to go to the gym?", "The time you can repeat every week. Strength can be slightly higher in the late afternoon, but the difference is small compared with the benefit of a time that reliably fits your life."),
  ("When is the gym least busy?", "Usually mid-morning, early afternoon on weekdays, and the last hour or two before closing. Friday evenings and Sunday afternoons are often quiet too."),
  ("What time is the gym busiest?", "Weekday evenings from about 5pm to 8pm, especially on Mondays and Tuesdays, and throughout January."),
  ("Is it better to work out in the morning or evening?", "Neither is clearly better for results. Mornings are easier to protect from the rest of the day. Evenings suit people who feel stronger later, but are easier to skip."),
 ],
 "related": ["how-often-should-you-go-to-the-gym", "gym-anxiety", "how-long-should-a-gym-session-be"],
},
{
 "slug": "how-many-rest-days-a-week",
 "title": "How many rest days a week do you need? A guide to gym rest days",
 "short": "How many rest days a week?",
 "h1": "How many rest days a week do you need?",
 "kicker": "Why rest days count, and how to place them",
 "desc": "Most people need one to three rest days a week. How to place rest days around your gym sessions, what to do on them, and why a rest day isn’t a missed day.",
 "card": "One to three for most people, how to place them, and why they count.",
 "published": "2026-10-30",
 "body": """
  <p><strong>Short answer: most people do well with one to three rest days a week.</strong> If you go to the gym two or three times a week, you already have them. If you go five or six times, plan at least one full rest day and avoid training the same muscles hard on consecutive days.</p>

  <h2>Why rest days matter</h2>
  <p>Training is the signal; recovery is when you actually adapt. Muscles repair and get stronger in the days after a session, not during it. Without enough rest, sessions start to feel heavier, sleep can suffer, and small aches turn into reasons to stop.</p>
  <p>There’s a habit reason too. A plan with rest built in is one you can keep for years. A plan that needs you every day is one bad week from collapse.</p>

  <h2>How many rest days, by schedule</h2>
  <div class="tablewrap"><table><thead><tr><th>Gym days</th><th>Rest days</th><th>Notes</th></tr></thead><tbody>
  <tr><td>2</td><td>5</td><td>Plenty of recovery. Full-body sessions work well.</td></tr>
  <tr><td>3</td><td>4</td><td>A rest day between each session is the classic layout.</td></tr>
  <tr><td>4</td><td>3</td><td>Use an upper/lower split so back-to-back days hit different muscles.</td></tr>
  <tr><td>5–6</td><td>1–2</td><td>Needs a split and sensible intensity. Keep at least one full rest day.</td></tr>
  </tbody></table></div>
  <p>The usual advice is to leave about 48 hours before training the same muscle group hard again. That’s why splits exist: legs on Monday, upper body on Tuesday, and neither is training through the other’s recovery.</p>
  <p>For ready-made weekly layouts, see <a href="how-often-should-you-go-to-the-gym">how often to go to the gym</a>.</p>

  <h2>Signs you need more rest</h2>
  <ul>
    <li>Your usual weights feel heavier for more than a session or two.</li>
    <li>Soreness hasn’t faded by the next time you train that area.</li>
    <li>You’re sleeping badly or feel flat for days.</li>
    <li>You’re dreading sessions you used to look forward to.</li>
  </ul>
  <p>Any of these is a reason to take an extra day, not to push through. Pain that’s sharp or doesn’t go away is a reason to speak to a GP or physio.</p>

  <h2>What to do on a rest day</h2>
  <p>Rest doesn’t have to mean the sofa, though it can. Walking, an easy cycle, a swim or some stretching all help you feel better without getting in the way of recovery. They also count towards the NHS’s 150 minutes of weekly activity.</p>

  <h2>A rest day isn’t a missed day</h2>
  <p>This is where daily streaks get it wrong. They treat the day you’re supposed to rest as a failure, which nudges people to train when they shouldn’t, or to feel bad when they don’t. Counting your week instead (“did I hit three this week?”) puts rest back where it belongs: in the plan.</p>
""",
 "faq": [
  ("How many rest days a week do I need?", "Most people do well with one to three. If you train two or three times a week you already have enough. If you train five or six times, keep at least one full rest day."),
  ("Is it OK to go to the gym every day?", "It can be if you vary the muscles you train and keep intensity sensible, but most people get better results and stick with it longer with at least one rest day a week."),
  ("How long should you rest between training the same muscle?", "The usual advice is about 48 hours before training the same muscle group hard again."),
  ("What should I do on a rest day?", "Anything easy: walking, a gentle cycle or swim, stretching, or genuinely resting. Light activity can help you recover and counts towards your weekly activity."),
 ],
 "related": ["how-often-should-you-go-to-the-gym", "how-long-should-a-gym-session-be", "how-long-to-see-results-from-the-gym"],
},
{
 "slug": "how-long-should-a-gym-session-be",
 "title": "How long should a gym session be? (Shorter than you think)",
 "short": "How long should a gym session be?",
 "h1": "How long should a gym session be?",
 "kicker": "And why a short session still counts",
 "desc": "Most effective gym sessions take 45 to 60 minutes, and 20 to 30 minutes is enough on a busy day. How long to spend at the gym, and why short sessions still count.",
 "card": "45 to 60 minutes is plenty, and 20 still counts.",
 "published": "2026-10-30",
 "body": """
  <p><strong>Short answer: 45 to 60 minutes is plenty for most people, and 20 to 30 minutes is a perfectly good session on a busy day.</strong> Past about an hour, most people are chatting, scrolling or resting longer, not training harder.</p>

  <h2>What fits in an hour</h2>
  <ul>
    <li><strong>5–10 minutes</strong> warming up.</li>
    <li><strong>30–45 minutes</strong> on four to six exercises, a few sets each, with sensible rests.</li>
    <li><strong>5 minutes</strong> cooling down or stretching, if you like to.</li>
  </ul>
  <p>Rest between sets is what stretches sessions out. Heavy compound lifts need two or three minutes; most other exercises need a minute or so. Supersets (alternating two exercises that use different muscles) are the easiest way to save time.</p>

  <h2>The 30-minute session</h2>
  <p>When the day’s gone wrong, a short session beats no session. Pick two or three big movements (a squat or leg press, a push and a pull), do a few hard sets of each, and leave. You’ll have done most of what mattered.</p>
  <p>Short sessions also protect the habit. The cue (it’s Wednesday, I go to the gym) gets repeated either way, and repetition is what makes it automatic. More on that in <a href="how-long-does-it-take-to-form-a-habit">how long a habit takes to form</a>.</p>

  <h2>How it adds up over a week</h2>
  <p>The <a href="https://www.nhs.uk/live-well/exercise/physical-activity-guidelines-for-adults-aged-19-to-64/" rel="noopener">NHS guidance</a> is strength work on at least two days, plus 150 minutes of moderate activity across the week. Three 45-minute sessions and some walking get you there comfortably. You don’t need long sessions; you need regular ones. See <a href="how-often-should-you-go-to-the-gym">how often to go</a>.</p>

  <h2>When longer makes sense</h2>
  <p>Longer sessions are fine if you enjoy them, train for a specific sport, or combine weights with a long cardio block. Just don’t let the idea that a “proper” session is 90 minutes stop you from going when you only have 30.</p>
""",
 "faq": [
  ("How long should a gym session be?", "45 to 60 minutes is plenty for most people. 20 to 30 minutes is a perfectly good session when you're short of time."),
  ("Is 30 minutes at the gym enough?", "Yes. Two or three big exercises with a few hard sets each covers most of what matters, and keeps the habit going on a busy day."),
  ("Is a 2-hour gym session too long?", "For most people, yes. Beyond about an hour, extra time tends to go on longer rests rather than more useful training."),
 ],
 "related": ["how-often-should-you-go-to-the-gym", "how-many-rest-days-a-week", "best-time-to-go-to-the-gym"],
},
{
 "slug": "gym-anxiety",
 "title": "Gym anxiety: how to start going when you feel out of place",
 "short": "Gym anxiety",
 "h1": "Gym anxiety: how to start going when you feel out of place",
 "kicker": "Practical ways through your first few weeks",
 "desc": "Gym anxiety is common, especially at first. Practical ways to make your first time at the gym easier: quiet times, a written plan, an induction, and small first visits.",
 "card": "Nerves are normal. Practical ways through your first few weeks.",
 "published": "2026-10-30",
 "body": """
  <p><strong>Feeling nervous about the gym is extremely common, and it fades with familiarity faster than almost anything else.</strong> Almost everyone there is thinking about their own session, not yours. The goal for the first few weeks isn’t a great workout. It’s to make the place feel ordinary.</p>

  <h2>Why it happens</h2>
  <p>Gym anxiety (sometimes called “gymtimidation”) usually comes from a few specific worries: not knowing how the equipment works, feeling watched, not knowing the unwritten rules, or feeling like you don’t look the part. Each one has a practical fix.</p>

  <h2>Before your first visit</h2>
  <h3>Go at a quiet time</h3>
  <p>Mid-morning and early afternoon on weekdays, or the last hour before closing, are usually calm. Avoid weekday evenings from 5pm to 8pm and January, at least at first. <a href="best-time-to-go-to-the-gym">When gyms are quietest</a> has more.</p>

  <h3>Book the induction</h3>
  <p>Most gyms offer a free induction when you join. Someone shows you round, explains the machines and answers questions. It turns the unknown into somewhere you’ve already been.</p>

  <h3>Write a short plan</h3>
  <p>Three or four exercises on your phone, with sets and reps. Knowing what you’re doing next removes most of the hovering, and the hovering is what feels conspicuous.</p>

  <h2>Your first few sessions</h2>
  <ul>
    <li><strong>Start with machines.</strong> They have instructions on the side and guide the movement for you.</li>
    <li><strong>Keep it short.</strong> Twenty or thirty minutes is a successful first visit. See <a href="how-long-should-a-gym-session-be">how long a session should be</a>.</li>
    <li><strong>Wear headphones.</strong> They help you stay in your own head and signal you’re busy.</li>
    <li><strong>Learn the basic etiquette.</strong> Wipe down equipment, put weights back, and ask “how many sets have you got left?” if you want to share. That’s most of it.</li>
    <li><strong>Go back soon.</strong> The second visit is far easier than the first, and the fifth is easier still. Familiarity is the cure.</li>
  </ul>

  <h2>How to start going to the gym and keep going</h2>
  <p>Pick a small, fixed plan: two days a week, the same days, the same time. Small and fixed beats ambitious and vague, especially when nerves are part of it. <a href="how-often-should-you-go-to-the-gym">How often to go</a> has a few simple schedules.</p>
  <p>If anxiety is getting in the way of more than the gym, it’s worth talking to your GP. The <a href="https://www.nhs.uk/mental-health/conditions/generalised-anxiety-disorder/overview/" rel="noopener">NHS pages on anxiety</a> are a good place to start.</p>
""",
 "faq": [
  ("How do I get over gym anxiety?", "Make the gym familiar: go at a quiet time, book the free induction, take a short written plan, start with machines and keep first visits short. It eases quickly with repeat visits."),
  ("What should I do on my first time at the gym?", "Keep it simple: a short warm-up, three or four machine exercises from a written plan, and 20 to 30 minutes in total. The aim is to leave feeling it was manageable."),
  ("When is the gym quietest for beginners?", "Usually mid-morning and early afternoon on weekdays, and the last hour or two before closing."),
 ],
 "related": ["best-time-to-go-to-the-gym", "how-long-should-a-gym-session-be", "how-often-should-you-go-to-the-gym"],
},
{
 "slug": "how-long-to-see-results-from-the-gym",
 "title": "How long does it take to see results from the gym?",
 "short": "How long to see results from the gym?",
 "h1": "How long does it take to see results from the gym?",
 "kicker": "What changes first, and what takes longer",
 "desc": "You’ll feel stronger within a few weeks and see visible changes after roughly two to three months of regular training. What changes when, and what speeds it up.",
 "card": "Stronger in weeks, visible in months, and what actually speeds it up.",
 "published": "2026-10-30",
 "body": """
  <p><strong>Short answer: you’ll feel stronger within two to four weeks, and most people see visible changes after two to three months of regular training.</strong> The timeline depends far more on how consistently you go than on what programme you follow.</p>

  <h2>What changes, and when</h2>
  <div class="tablewrap"><table><thead><tr><th>When</th><th>What you’ll notice</th></tr></thead><tbody>
  <tr><td>Weeks 1–2</td><td>Soreness after sessions, which eases quickly. Movements start to feel less awkward.</td></tr>
  <tr><td>Weeks 2–6</td><td>Weights go up week on week. This is mostly your nervous system learning to use the muscle you already have.</td></tr>
  <tr><td>Weeks 8–12</td><td>Muscle growth becomes visible for most people. Clothes fit differently. Everyday things (stairs, carrying shopping) feel easier.</td></tr>
  <tr><td>6–12 months</td><td>Clear, lasting changes in strength and shape, if you’ve kept going.</td></tr>
  </tbody></table></div>
  <p>Everyone’s timeline is different. Age, sleep, diet, starting point and genetics all play a part, and progress is rarely a straight line.</p>

  <h2>Why most people don’t see results</h2>
  <p>It’s rarely the programme. It’s usually that they stopped going in week five, before the visible part started. The weeks where you’re getting stronger but don’t look different are exactly when motivation dips.</p>
  <p>That gap lines up with how long a habit takes to form: around two months on average, longer for exercise. Getting through it is most of the job. See <a href="how-long-does-it-take-to-form-a-habit">how long it takes to form a habit</a>.</p>

  <h2>What speeds it up</h2>
  <ul>
    <li><strong>Consistency.</strong> Two or three sessions every week, for months, beats any burst. <a href="how-often-should-you-go-to-the-gym">How often to go</a>.</li>
    <li><strong>Progressive overload.</strong> Gradually adding weight, reps or sets over time.</li>
    <li><strong>Enough protein and sleep.</strong> Recovery is when you adapt; see <a href="how-many-rest-days-a-week">rest days</a>.</li>
    <li><strong>Patience with the scale.</strong> Weight can stay flat while you lose fat and gain muscle. Strength and how clothes fit are better signals early on.</li>
  </ul>

  <h2>Measure turning up, not just the mirror</h2>
  <p>The mirror lags behind. The one number you control every week is whether you went. Track that, and the visible results follow on their own timetable.</p>
""",
 "faq": [
  ("How long does it take to see results from the gym?", "Most people feel stronger within two to four weeks and see visible changes after about two to three months of regular training."),
  ("Why am I not seeing results from the gym?", "Usually because it's still early or sessions have been irregular. Strength rises first; visible change typically takes eight to twelve weeks of consistent training."),
  ("How long does it take to build muscle?", "Visible muscle growth usually takes around eight to twelve weeks of regular strength training, with clearer changes over six to twelve months."),
 ],
 "related": ["how-long-does-it-take-to-form-a-habit", "how-often-should-you-go-to-the-gym", "how-many-rest-days-a-week"],
},
{
 "slug": "how-to-build-a-gym-habit",
 "title": "How to build a gym habit that survives a bad week",
 "short": "How to build a gym habit",
 "h1": "How to build a gym habit (that survives a bad week)",
 "kicker": "Seven rules for turning up, from the research",
 "desc": "How to make going to the gym a habit: pick a number you can keep, fix the days, lower the bar, count weeks not days, and expect it to take a couple of months.",
 "card": "Seven rules for turning up, and why most attempts stop in week three.",
 "published": "2026-10-30",
 "body": """
  <p><strong>Short answer: pick a small weekly target, tie it to fixed days and times, make each visit easy to start, and judge yourself by the week, not the day.</strong> Expect it to take a couple of months before it feels automatic. Most attempts fail in the slow middle, not at the start.</p>

  <h2>1. Pick a number you can keep in a bad week</h2>
  <p>Set your weekly target from an ordinary, slightly-too-busy week, not from your most motivated Monday. For most people that’s two or three visits. Going more than you planned feels good; going less than you planned feels like failure, even when you still went. More in <a href="how-often-should-you-go-to-the-gym">how often to go</a>.</p>

  <h2>2. Fix the days and a rough time</h2>
  <p>Habits form around a cue. “Monday, Wednesday and Friday after work” becomes automatic far faster than “three times a week, whenever”. Deciding once means you’re not negotiating with yourself every morning. If you’re unsure when, see <a href="best-time-to-go-to-the-gym">the best time to go</a>.</p>

  <h2>3. Make turning up the whole goal</h2>
  <p>The habit is going, not the workout. On a tired day, a 20-minute session still repeats the cue and keeps the pattern alive. Lower the bar until you can clear it on your worst day; the good days will take care of themselves. See <a href="how-long-should-a-gym-session-be">how long a session needs to be</a>.</p>

  <h2>4. Remove the friction before it starts</h2>
  <ul>
    <li>Pack your bag the night before and leave it by the door.</li>
    <li>Choose a gym on your normal route, not the nicer one across town.</li>
    <li>Have a short written plan, so you never stand around wondering what to do.</li>
  </ul>

  <h2>5. Count weeks, not days</h2>
  <p>A daily streak breaks on your first rest day, which is the day you’re meant to rest. A weekly count asks a fairer question: did you hit your number this week? A bad week then costs one week, not the whole thing. <a href="how-many-rest-days-a-week">Rest days</a> belong in the plan.</p>

  <h2>6. Treat a missed session as weather</h2>
  <p>In the best-known study of habit formation, from UCL, missing a single day didn’t meaningfully set people back. What breaks habits is the story you tell after a miss (“I’ve blown it”), not the miss itself. Shrug, and go on the next planned day.</p>

  <h2>7. Expect it to take about two months</h2>
  <p>The same study found a median of 66 days for a behaviour to feel automatic, and exercise sat at the slow end. If week three still takes effort, nothing is wrong; that’s the normal part of the curve. More in <a href="how-long-does-it-take-to-form-a-habit">how long a habit takes to form</a>.</p>

  <h2>If nerves are what stop you</h2>
  <p>Gym anxiety is common and fades quickly with familiarity. Going at quiet times and keeping first visits short helps most. See <a href="gym-anxiety">gym anxiety</a>.</p>
""",
 "faq": [
  ("How do I make going to the gym a habit?", "Pick a small weekly target you can keep in a busy week, fix the days and a rough time, make each visit easy to start, count weeks rather than days, and expect it to take around two months to feel automatic."),
  ("How many days does it take to build a gym habit?", "Around two months on average. In a UCL study the median was 66 days, with a wide range, and exercise habits took longer than simpler ones."),
  ("What if I miss a session?", "Carry on with the next planned day. Missing a single session doesn't meaningfully set a habit back; giving up afterwards does."),
  ("Is there an app that helps you build a gym habit?", "Cadence is a gym habit app for iPhone that notices when you arrive at your gym and counts the visit automatically. No workout logging. It uses a weekly target and a weekly streak, with one missed week a month forgiven."),
 ],
 "related": ["how-long-does-it-take-to-form-a-habit", "how-often-should-you-go-to-the-gym", "gym-anxiety"],
},
{
 "section": "compare",
 "slug": "gym-apps-compared",
 "title": "Gym apps compared: workout loggers, habit trackers and Cadence",
 "short": "Gym apps compared",
 "h1": "Gym apps compared: which kind do you actually need?",
 "kicker": "Workout loggers, habit trackers and gym habit apps",
 "desc": "An honest comparison of gym apps: workout loggers like Strong, Hevy and Fitbod, habit trackers like Streaks, and Cadence, which counts gym visits automatically.",
 "card": "Loggers, habit trackers and Cadence, and who each one suits.",
 "published": "2026-10-30",
 "body": """
  <p><strong>Short answer: if your problem is what to do in the gym, use a workout logger like Strong, Hevy or Fitbod. If your problem is getting there at all, use a habit app like Cadence. Plenty of people use one of each.</strong> Most “best gym apps” lists only cover the first kind.</p>
  <p>We make Cadence, so read this with that in mind. We’ve tried to be fair about what the others do well, and about what Cadence doesn’t do. Features and prices change, so check each app’s App Store page.</p>

  <h2>The three kinds of gym app</h2>
  <h3>Workout loggers</h3>
  <p>You record each exercise, set, rep and weight. They show your history and progress over time, and some suggest what to do next. Good for anyone who already goes and wants to get stronger in a structured way. They need input every session.</p>

  <h3>General habit trackers</h3>
  <p>You tick off any habit you choose: water, reading, the gym. Flexible, often beautifully designed, and good for tracking many habits in one place. Usually you mark the gym as done yourself, and most count daily streaks.</p>

  <h3>Gym habit apps</h3>
  <p>Built for the single question “did I go?”. Cadence notices when you arrive at your gym and counts the visit automatically, so there’s nothing to tick. It doesn’t record what you do inside.</p>

  <h2>Side by side</h2>
  <div class="tablewrap"><table><thead><tr><th>App</th><th>Kind</th><th>Best for</th><th>How the gym gets recorded</th></tr></thead><tbody>
  <tr><td><strong>Strong</strong></td><td>Workout logger</td><td>Simple, fast logging of lifts and progress</td><td>You log each set</td></tr>
  <tr><td><strong>Hevy</strong></td><td>Workout logger</td><td>Logging with a social feed and shared routines</td><td>You log each set</td></tr>
  <tr><td><strong>Fitbod</strong></td><td>Workout planner and logger</td><td>Generated workouts that adapt to your history</td><td>You follow and log the plan</td></tr>
  <tr><td><strong>Streaks</strong></td><td>Habit tracker (iPhone)</td><td>Tracking a handful of daily habits; some can complete from Apple Health</td><td>You tick it, or it completes from Health data</td></tr>
  <tr><td><strong>Cadence</strong></td><td>Gym habit app (iPhone)</td><td>Building the habit of turning up, with nothing to log</td><td>Automatically, when you arrive at your gym</td></tr>
  </tbody></table></div>

  <h2>Which should you use?</h2>
  <ul>
    <li><strong>You go regularly and want to get stronger:</strong> a workout logger. Strong if you want it simple, Hevy if you like the social side, Fitbod if you want the plan written for you.</li>
    <li><strong>You want one app for lots of habits:</strong> a general habit tracker such as Streaks.</li>
    <li><strong>You keep meaning to go and don’t:</strong> Cadence. It’s built for the part before the workout, and it never asks you to log anything.</li>
    <li><strong>Both:</strong> Cadence to get you there, a logger once you’re inside. They don’t overlap.</li>
  </ul>

  <h2>What Cadence doesn’t do</h2>
  <p>No exercise library, no sets or reps, no workout plans, no calories, no social feed. It doesn’t track runs or home workouts; it counts visits to the gym you choose. If you need any of those, pair it with a logger. Read <a href="cadence-vs-strong">Cadence vs Strong</a> and <a href="cadence-vs-streaks">Cadence vs Streaks</a> for the detail.</p>
""",
 "faq": [
  ("What is the best gym app?", "It depends on the problem. For logging workouts and progress, apps like Strong, Hevy and Fitbod are popular. For building the habit of actually going, Cadence is a gym habit app for iPhone that notices when you arrive at your gym and counts the visit automatically. No workout logging."),
  ("Is there an app that tracks gym visits automatically?", "Yes. Cadence uses your phone's geofencing to notice when you arrive at your chosen gym, and counts a stay of 20 minutes or more as a visit, even with the app closed."),
  ("Can I use Cadence with Strong or Hevy?", "Yes. Cadence counts whether you went; a logger records what you did. They don't overlap."),
 ],
 "related": ["cadence-vs-strong", "cadence-vs-streaks", "how-to-build-a-gym-habit"],
},
{
 "section": "compare",
 "slug": "cadence-vs-streaks",
 "title": "Cadence vs Streaks: which habit app is better for the gym?",
 "short": "Cadence vs Streaks",
 "h1": "Cadence vs Streaks",
 "kicker": "Two iPhone habit apps, built for different jobs",
 "desc": "Cadence vs Streaks for building a gym habit: Streaks tracks many daily habits you tick off; Cadence counts gym visits automatically with a weekly target.",
 "card": "A general habit tracker against one built only for the gym.",
 "published": "2026-10-30",
 "body": """
  <p><strong>Short answer: Streaks is a general habit tracker for a handful of daily habits. Cadence does one thing: it notices when you arrive at your gym and counts the visit, against a weekly target. If the gym is the habit you care about, Cadence fits it more closely. If you want one app for many habits, Streaks does more.</strong></p>
  <p>We make Cadence. Streaks is a well-made, long-established app, and we’ve tried to describe it fairly; check its App Store page for current features and price.</p>

  <div class="tablewrap"><table><thead><tr><th></th><th>Cadence</th><th>Streaks</th></tr></thead><tbody>
  <tr><td>Built for</td><td>Going to the gym</td><td>Any daily habit</td></tr>
  <tr><td>Recording a visit</td><td>Automatic, when you arrive at your gym</td><td>Tick it off, or complete it from Apple Health data</td></tr>
  <tr><td>Target</td><td>Visits per week, on days you choose</td><td>Daily, or a number of times per week</td></tr>
  <tr><td>Missed days</td><td>Streak counted in weeks; one missed week a month forgiven</td><td>Streak-based, with options for skipping days</td></tr>
  <tr><td>Reminders</td><td>Short nudges on planned days, never a telling-off</td><td>Reminders per task</td></tr>
  <tr><td>Other habits</td><td>No, gym only</td><td>Yes, many</td></tr>
  <tr><td>Price</td><td>Free; Plus is optional</td><td>Paid app</td></tr>
  </tbody></table></div>

  <h2>Where Streaks is better</h2>
  <p>Tracking several habits in one place, with a lot of flexibility over how each one counts. If “gym” is one line on a list of ten, Streaks is the better home for it.</p>

  <h2>Where Cadence is better</h2>
  <p>The gym specifically. Because it counts the visit when you arrive, there’s nothing to remember to tick, and it can’t be ticked from the sofa. The weekly target and forgiving weekly streak suit the gym, where rest days are part of the plan rather than a break in the chain. See <a href="how-to-build-a-gym-habit">how to build a gym habit</a> for why that matters.</p>

  <h2>Can you use both?</h2>
  <p>Yes. Some people keep Streaks for everything else and let Cadence handle the gym.</p>
""",
 "faq": [
  ("Is Cadence or Streaks better for the gym?", "For the gym alone, Cadence fits more closely: it counts visits automatically when you arrive and uses a weekly target. Streaks is better if you want to track many different habits in one app."),
  ("Does Streaks track gym visits automatically?", "Streaks can complete some tasks from Apple Health data, such as workouts. Cadence counts a visit when you physically arrive at your chosen gym, using geofencing."),
 ],
 "related": ["gym-apps-compared", "cadence-vs-strong", "how-to-build-a-gym-habit"],
},
{
 "section": "compare",
 "slug": "cadence-vs-strong",
 "title": "Cadence vs Strong: do you need a workout logger or a gym habit app?",
 "short": "Cadence vs Strong",
 "h1": "Cadence vs Strong",
 "kicker": "Getting there, and what you do when you’re there",
 "desc": "Cadence vs Strong: Strong logs your sets, reps and weights; Cadence counts gym visits automatically to build the habit of going. They solve different problems and work well together.",
 "card": "Not rivals: one gets you there, the other logs the lifting.",
 "published": "2026-10-30",
 "body": """
  <p><strong>Short answer: they don’t compete. Strong is a workout logger for recording sets, reps and weights. Cadence is a gym habit app that counts your visits automatically. Strong helps you once you’re in the gym; Cadence helps you get there. Many people would be well served by both.</strong></p>
  <p>We make Cadence. Strong is a popular, well-regarded logger; check its App Store page for current features and price.</p>

  <div class="tablewrap"><table><thead><tr><th></th><th>Cadence</th><th>Strong</th></tr></thead><tbody>
  <tr><td>Answers</td><td>Did I go this week?</td><td>What did I lift, and am I getting stronger?</td></tr>
  <tr><td>Input needed</td><td>None after setup</td><td>Every set, every session</td></tr>
  <tr><td>Records</td><td>Visits: arrival and departure times</td><td>Exercises, sets, reps, weights, history</td></tr>
  <tr><td>Best for</td><td>People who struggle to go consistently</td><td>People who already go and want structured progress</td></tr>
  <tr><td>Price</td><td>Free; Plus is optional</td><td>Free to start, with a paid tier</td></tr>
  </tbody></table></div>

  <h2>Choose Strong if</h2>
  <p>You go reliably and want to track progressive overload: adding weight or reps over time, seeing personal records, and following a programme.</p>

  <h2>Choose Cadence if</h2>
  <p>The hard part is turning up. Cadence asks for nothing in the gym, so it works even on the days you’d never open a logger. It nudges you on planned days and counts weeks, not days, so a rest day never breaks anything.</p>

  <h2>Using both</h2>
  <p>Cadence gets you through the door; Strong records the session. Neither duplicates the other. If you’re early in building the habit, start with Cadence alone and add a logger once going feels normal; see <a href="how-long-does-it-take-to-form-a-habit">how long that usually takes</a>.</p>
""",
 "faq": [
  ("Is Cadence a replacement for Strong?", "No. Strong logs workouts; Cadence counts gym visits automatically to help you build the habit of going. They solve different problems and work together."),
  ("Do I need a workout logger to build a gym habit?", "Not at first. Logging every set can be one more barrier when the hard part is turning up. Many people start by just tracking visits and add a logger later."),
 ],
 "related": ["gym-apps-compared", "cadence-vs-streaks", "how-long-to-see-results-from-the-gym"],
},
]
