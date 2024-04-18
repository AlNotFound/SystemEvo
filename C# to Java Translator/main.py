from Lexer import Lexer
from Parser import Parser
from CodeGenerator import CodeGenerator
from Exceptions import *
from SemanticAnalyzer import SemanticAnalyzer
from OptimizeCode import OptimizeCode

from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import Label
from tkinter import Button
from tkinter import Entry
import tkinter as tk
import pathlib

root = tk.Tk()
#Входные и выходные файлы
INPUT_PATH = "file.txt"
LEXER_OUTPUT_PATH = "lexer_output.txt"
PARSER_OUTPUT_PATH = "parser_output.txt"
SEMANTIC_ANALYZER_OUTPUT_PATH = "semantic_output.txt"
GENERATED_CODE_PATH = "generated_code.txt"
OPTIMIZED_OUTPUT_PATH = "optimized_output.txt"
ENCODING = "utf-8"

#Раздел функций работы интерфейса
def open_file():
  file_path = filedialog.askopenfilename(
    title="Select a Text File", filetypes=[("Text files", "*.txt")])
  if file_path:
    with open(file_path, 'r') as file:
      content = file.read()
      txtc.delete(1.0, tk.END)  # Clear previous content
      txtc.insert(tk.END, content)

def save_file():
  directory = "D:\\"
  filepath = directory + namefile.get() + ".txt"
  pathlib.Path(filepath).touch()
  with open(filepath, 'w') as fp:
    fp.write(txtj.get(1.0, tk.END))
    fp.close()

def translation():
  my_file = open("file.txt", "w")
  my_file.write(txtc .get(1.0, tk.END))
  my_file.close()
  with (
    open(INPUT_PATH, "r", encoding=ENCODING) as in_file,
    open(LEXER_OUTPUT_PATH, "w", encoding=ENCODING) as lexer_file
  ):
    lexer = Lexer(in_file)
    lexer.print_all_tokens(file=lexer_file)

  with (
    open(INPUT_PATH, "r", encoding=ENCODING) as in_file,
    open(PARSER_OUTPUT_PATH, "w", encoding=ENCODING) as parser_file
  ):
    lexer = Lexer(in_file)
    parser = Parser(lexer)
    syntax_tree = parser.parse()
    print(syntax_tree, file=parser_file)

  with (
    open(INPUT_PATH, "r", encoding=ENCODING) as in_file,
    open(SEMANTIC_ANALYZER_OUTPUT_PATH, "w", encoding=ENCODING) as semantic_file
  ):
    lexer = Lexer(in_file)
    parser = Parser(lexer)
    tree = parser.parse()
    semantic = SemanticAnalyzer()
    scope = semantic.analyze(tree)
    scope.print(file=semantic_file)

  with (
    open(INPUT_PATH, "r", encoding=ENCODING) as in_file,
    open(GENERATED_CODE_PATH, "w", encoding=ENCODING) as generate_file
  ):
    lexer = Lexer(in_file)
    parser = Parser(lexer)
    tree = parser.parse()
    code_generation = CodeGenerator(tree)
    print(code_generation, file=generate_file)

  with (
    open(OPTIMIZED_OUTPUT_PATH, "w", encoding=ENCODING) as optimize_file
  ):
    optimized_code = OptimizeCode(scope, tree, optimize_file)
    optimized_code.print()

  file_path = "generated_code.txt"
  with open(file_path, 'r') as file:
    content = file.read()
    txtj.delete(1.0, tk.END)  # Clear previous content
    txtj.insert(tk.END, content)

 #размер окна
root.geometry('1350x800')

root.title("Транслятор С# в Java")
#Отрисовка интерфейса
lbl = Label(root, text="C#", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)

lbl = Label(root, text="Java", font=("Arial Bold", 20))
lbl.grid(column=2, row=0)

txtc = scrolledtext.ScrolledText(root, width=75, height=40)
txtc.grid(column=0, row=1)

txtc.focus()  # сразу курс в текстовом поле
btnl = Button(root,  text="Импорт с файла", command=open_file)
btnl.grid(column=0, row=2)

btnmain = Button(root,  text="Транслировать", command=translation)
btnmain.grid(column=1, row=1)

txtj = scrolledtext.ScrolledText(root, width=75, height=40,)
txtj.grid(column=2, row=1)

lbl = Label(root, text="название файла для сохранения", font=("Arial Bold", 14))
lbl.grid(column=2, row=2)

namefile = Entry(root,width=10)
namefile.grid(column=2, row=3)

btnr = Button(root, text="Сохранить файл", command=save_file)
btnr.grid(column=2, row=4)

root.mainloop()




