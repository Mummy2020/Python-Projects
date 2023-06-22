from django.db import models

class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    campus_ID = models.IntegerField(default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)


    # Create model manager
    object = models.Manager()

    # Display the object output values in the form of a string
    def __str__(self):
        # Returns the input value of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_name = '{0.campus_name}: {0.state}'
        return display_name.format(self)

    # Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"

