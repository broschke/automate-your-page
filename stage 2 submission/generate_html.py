def html(id,sub,des):
    return '''
    <div>
        <h2 class="subheader" id="lesson'''+id+'"'+'>'+sub+'''</h2>
    </div>
    <div class="description">'''+des+'''
    </div>'''


def get_subheader(concept):
	sub_start = concept.find('SUBHEADER:')
	sub_end = concept.find('ID:')
	sub_header = concept[sub_start+11:sub_end-1]
	return sub_header

def get_id(concept):
	id_start = concept.find('ID:')
	id_end = concept.find('DESCRIPTION:')
	id = concept[id_start+4:id_end-1]
	return id
	
def get_description(concept):
	desc_start = concept.find('DESCRIPTION:')
	desc = concept[desc_start+13:]
	return desc
	
def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('SUBHEADER:')
        next_concept_end   = text.find('SUBHEADER:', next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept
    
text_to_convert = '''SUBHEADER: Automate Your Page - Lesson Four
ID: 2-4
DESCRIPTION: Python's If statement checks if a condition is True or False and performs a block of code based on the resulting boolean. Like Functions and While loops, If statements are written with a colon at the end.
SUBHEADER: Automate Your Page - Lesson Five
ID: 2-5
DESCRIPTION: Lists are a collection of items within one object. Lists are created with brackets and items are separated with commas. A list can have a list inside it, or nested. They can be assigned to variables.'''

def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        subheader = get_subheader(concept)
        description = get_description(concept)
        id = get_id(concept)
        concept_html = html(id, subheader, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(text_to_convert)
