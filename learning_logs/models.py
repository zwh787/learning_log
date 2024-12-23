from django.db import models

# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
      verbose_name_plural = 'entries'
    def __str__(self):
      """返回一个表示条目的简单字符串"""
      if len(self.text) > 50:
         return self.text[:50] + '...'  # 如果超过 50 个字符，则截断并添加省略号
      return self.text  # 否则直接返回文