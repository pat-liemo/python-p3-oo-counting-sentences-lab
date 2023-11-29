#!/usr/bin/env python3

class MyString:
  
  def __init__(self, value: str = ""):
    self._value = value
    
  def getter(self):
    return self._value
  
  def setter(self, value):
    if (type(value) == str):
      self._value = value
    else:
      print("The value must be a string.")
      
  def is_sentence(self):
    if self._value.endswith("."):
      return True
    else:
      return False
      
  def is_question(self):
    if self._value.endswith("?"):
      return True
    else:
      return False
      
  def is_exclamation(self):
    if self._value.endswith("!"):
      return True
    else:
      return False
      
  def count_sentences(self):
      cleaned_string = self._value.replace("!", ".").replace("?", ".")
              
      sentences = cleaned_string.split(".")

      valid_sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

      return len(valid_sentences)