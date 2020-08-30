from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your tests here.
class SeattleBlogTest(SimpleTestCase):

  def test_homepage_status(self):
    self.help_status_code('home')
  
  def test_hompage_template(self):
    self.check_template_used('home', 'home.html')

  def help_status_code(self, url_name):
    url = reverse(url_name)
    response =  self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def check_template_used(self, url_name, template):
    url = reverse(url_name)
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'base.html')
    self.assertTemplateUsed(response, template)


  class BlogTests(TestCase):

    def setup(self):
      self.user = get_user_model().objects.create_user(
        username = 'test',
        password = 'pass'
        )

      self.seattle_blog = SeattleBlog.objects.create(
          title = 'test title',
          author = self.user,
          body = 'test body',

      )
      self.seattle_blog.save()
      self.blog = SeattleBlog.objects.get(pk=1)

    def test_model_content(self):
      self.assertEqual(self.blog, self.seattle_blog)

    def test_model_title(self):
      self.assertEqaul(self.title, self.seattle_blog)

    def test_create_redirect_home(self): 
        response = self.client.post(reverse("Make_SeattleBlog"),{
            'title' : 'Test title', 
            'author' : self.user, 
            'body' : 'body',
        } 
        , follow=True)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed("home.html")
