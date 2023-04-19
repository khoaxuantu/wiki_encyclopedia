# Wiki Encyclopedia

A Wikipedia-like online encyclopedia

## Preview
![](/wiki_preview.png)

## Functionalities
- Users can view all available entries of of the encyclopedia via the home page
- Users can access to a entry page by clicking to its entry name
- Users can type a query into the search box
    + If the query matches the name of an encyclopeida entry, the user will be redirected to that entry's page
    + If the query does not match, users will be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring.
- Users can create a new encyclopedia entry
- Users can edit the content of an existing encyclopedia entry
- Users can access to a random encyclopedia entry via `Random Page`

## Tools
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

## Prerequisite
- Python 3.10
- Django 4.1.6
- Markdown2 2.4.7

## Run (local)
```bash
python3 manage.py runserver
```