from pathlib import Path
import sys

p=Path(sys.argv[1] if len(sys.argv)>1 else 'app/src/main/assets/www/index.html')
s=p.read_text(encoding='utf-8')

# Add revision marker once.
marker='<!-- TN Tamil terminology revision: v1.0.2 | Tamil Nadu school-biology aligned terminology -->\n'
if marker in s:
    # The workflow and local builds may invoke this tool more than once.  Once
    # the audited revision is present, preserve the verified document byte for
    # byte instead of nesting Tamil-first labels a second time.
    sys.exit(0)

if '<head>\n' not in s:
    raise SystemExit('Expected <head> marker not found; refusing partial patch')
s=s.replace('<head>\n','<head>\n'+marker,1)

# School-textbook-aligned terminology. Longer inflected forms first.
repls=[
    ('சிலியாக்களின்','குறுஇழைகளின்'),
    ('சிலியாக்களும்','குறுஇழைகளும்'),
    ('சிலியாக்களை','குறுஇழைகளை'),
    ('சிலியாக்களில்','குறுஇழைகளில்'),
    ('சிலியாக்களால்','குறுஇழைகளால்'),
    ('சிலியாக்கள்','குறுஇழைகள்'),
    ('ஒவ்வொரு சிலியமும்','ஒவ்வொரு குறுஇழையும்'),
    ('சிலியா அசைவு','குறுஇழைகளின் அசைவு'),
    ('சிலியா','குறுஇழை'),
    ('கொடிமயிர்களின்','கசையிழைகளின்'),
    ('கொடிமயிர்களும்','கசையிழைகளும்'),
    ('கொடிமயிர்களை','கசையிழைகளை'),
    ('கொடிமயிர்களில்','கசையிழைகளில்'),
    ('கொடிமயிர்களால்','கசையிழைகளால்'),
    ('கொடிமயிர்கள்','கசையிழைகள்'),
    ('கொடிமயிர்','கசையிழை'),
    ('புரவலர்','விருந்தோம்பி'),
    ('போலிசீலோம்','போலி உடற்குழி'),
    ('போலிக்குழி','போலி உடற்குழி'),
    ('சீலோம்','உடற்குழி'),
    ('பலவடிவத்தன்மை','பல்லுருவத் தன்மை'),
    ('பலவடிவத் தன்மை','பல்லுருவத் தன்மை'),
    ('பலவடிவம்','பல்லுருவம்'),
    ('கண்டவமைப்பு','கண்டங்களாதல்'),
    ('கண்டமுறை','கண்டங்களாதல்'),
]
for a,b in repls:
    s=s.replace(a,b)

# Tamil-first phylum labels in Tamil syllabus summaries.
phylum_summary=[
    ('Porifera வகுப்புகள்','துளையுடலிகள் (Porifera) வகுப்புகள்'),
    ('Cnidaria வகுப்புகள்','குழியுடலிகள் (Cnidaria) வகுப்புகள்'),
    ('Platyhelminthes வகுப்புகள்','தட்டைப்புழுக்கள் (Platyhelminthes) வகுப்புகள்'),
    ('Nematoda வகுப்புகள்','உருளைப்புழுக்கள் (Nematoda) வகுப்புகள்'),
    ('Annelida வகுப்புகள்','வளைத்தசைப் புழுக்கள் (Annelida) வகுப்புகள்'),
    ('Arthropoda வகுப்பு மேலோட்டம்','கணுக்காலிகள் (Arthropoda) வகுப்பு மேலோட்டம்'),
    ('Mollusca வகுப்புகள்','மெல்லுடலிகள் (Mollusca) வகுப்புகள்'),
    ('Echinodermata வகுப்புகள்','முட்தோலிகள் (Echinodermata) வகுப்புகள்'),
]
for a,b in phylum_summary:
    s=s.replace(a,b)

# Improve recurrent Tamil headings without altering English scientific text.
heading_repls=[
    ('போரிஃபெரா — பொதுப் பண்புகள்','துளையுடலிகள் (Porifera) — பொதுப் பண்புகள்'),
    ('நெமடோடா — பொதுப் பண்புகள்','உருளைப்புழுக்கள் (Nematoda) — பொதுப் பண்புகள்'),
    ('அன்னெலிடா — பொதுப் பண்புகள்','வளைத்தசைப் புழுக்கள் (Annelida) — பொதுப் பண்புகள்'),
    ('ஆர்த்ரோபோடா — பொதுப் பண்புகள்','கணுக்காலிகள் (Arthropoda) — பொதுப் பண்புகள்'),
    ('மொல்லஸ்கா — பொதுப் பண்புகள்','மெல்லுடலிகள் (Mollusca) — பொதுப் பண்புகள்'),
    ('எக்கைனோடெர்மேட்டா — பொதுப் பண்புகள்','முட்தோலிகள் (Echinodermata) — பொதுப் பண்புகள்'),
    ('அன்னெலிடாவின் கண்டங்களாதலும் வாழ்க்கை முறைகளும்','வளைத்தசைப் புழுக்களில் கண்டங்களாதலும் வாழ்க்கை முறைகளும்'),
]
for a,b in heading_repls:
    s=s.replace(a,b)

# Grammar repair after terminology substitution.
s=s.replace('குறுஇழைக்கள்','குறுஇழைகள்')
s=s.replace('குறுஇழை காணப்படும்','குறுஇழைகள் காணப்படும்')
s=s.replace('குறுஇழை புறணி','குறுஇழைப் புறணி')

p.write_text(s,encoding='utf-8')
