# headquater

**As** a User
**I want to** receive an article for provided group/tag
**so that** I can repeat material

Prerequisites: 
- crud for questions
- crud for answers

- Endpoint in article router
- Query that determines, which article has the biggest priority

Assumptions: 
- articles should be created properly, so that the whole article would be treated as a topic to repeat/learn
- in case, some article should be a subarticle, we can always assign it another/new tag. It allows to create artiles that will be used in diffrent tags

**As** a User
**I want to** submit my answers
**so that** the statistics can be updated

- Endpoint for receiving answers
- Based on answers and statistics, next repetition time should be calculated

**As** a User
**I want to** know knowledge level of a given group/tag
**so that** I can decide what should I take next

- Return a list of groups with knowledge level 







