from django import template

register = template.Library()

@register.filter
def pairElements(value):
    list = []
    for i in range(0,len(value),2):
        
        x = (value[i], value[i+1] if i+1 < len(value) else None)
        
        #if (i+1 < len(value)):
        #    x = (value[i], value[i+1])
        #else:
        #    x = (value[i], None)
        list.append(x)
    return list
        
    