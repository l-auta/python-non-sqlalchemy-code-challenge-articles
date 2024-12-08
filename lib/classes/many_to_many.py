class Article:

    all = []  #to store all the articles that are initiated

    def __init__(self, author, magazine, title):
        self._author = None  #put this way so that only when the author setter gets called a new author object will be created
        self.author = author
        self._magazine = None  #same as the author one
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property  #gets the _title
    def title(self):
        return self._title
    
    @title.setter  #sets the _title
    def title(self, value):
        if hasattr(self, '_title'):  #checks if the _title had already been set
            raise RuntimeError("The title of the article has already been set")
        if not isinstance(value, str) :  #ensures the title is a string
            raise TypeError("Tile should be a string ")
        if not (5 <= len(value) <=50):  #ensures the title has between 5 and 50 characters
            raise ValueError("The length should be between 5 and 50 characters")
        self._title = value

    @property  #gets the _author
    def author(self):
        return self._author
    
    @author.setter  #sets the _author
    def author(self, value):
        if not isinstance(value, Author):  #ensures the author is from an Author instance
            raise TypeError("Author must be an instance of class Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):  #ensures the value is initaited from class Magazine
            raise TypeError("Magazine must be an instance of class Magazine")
        self._magazine = value


        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):  #checks if there was already a _name set
            raise RuntimeError("Name has already been set")
        if not isinstance(value, str) or len(value) == 0 :  #ensures a length of more than 0 characters
            raise ValueError("Name must be a string and more than 0 characters long")
        self._name = value

    def articles(self):
        author_article = [article for article in Article.all if article.author == self]  #goes through the all attribute in Article and checks if the .author is self

        for article in author_article:  #basically the articles in all[]
            if not isinstance(article, Article):  #article should be an instance of class Article
                raise TypeError("The article should be an instance of class Article")
        
        return author_article

    def magazines(self):
         author_magazine = {article.magazine for article in Article.all if article.author == self}  #use of {} cuz here its not an article rather its the article.magazine

         for magazine in author_magazine:
            if not isinstance(magazine, Magazine):  #should be initialised from class Magazine
                raise TypeError("The article should be an instance of class Article")
        
         return author_magazine
    

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine): #initiated from the class Magazine
            raise TypeError("Magazine must be an instance of the Magazine class")
        
        new_article = Article(self, magazine, title) #the class article is called and given the 2 arguments of add_article
        return new_article

    def topic_areas(self):
        # Collect all magazines the author has contributed to
        articles_by_author = self.articles()  # Get all articles written by the author
        if not articles_by_author:
            return None  # If the author has no articles, return None
        
        # Use a set to collect unique categories of the magazines
        topic_areas = {article.magazine.category for article in articles_by_author}

        # Return the list of unique categories
        return list(topic_areas)

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) :  #the name should be a string
            raise TypeError("Name must be a string")
        if not (2 <= len(value) <= 16):  #the length of the name should be between 2 and 16 characters
            raise ValueError("Name should be betwwen 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:  #ensures it is a string and has more than 0 characters
            raise ValueError("The category of the magazine should be a string of more than 0 characters")
        self._category = value


    def articles(self):  #same for articles() in Author class
        magazine_article = [article for article in Article.all if article.magazine == self]  

        for article in magazine_article:
            if not isinstance(article, Article):
                raise TypeError("The article should be an instance of class Article")
        
        return magazine_article
        

    def contributors(self):  #same for magazines() in Author class
        magazine_authors = {article.author for article in Article.all if article.magazine == self}

        for author in magazine_authors:
            if not isinstance(author, Author):
                raise TypeError("The article should be an instance of class Article")
        
        return magazine_authors
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass


