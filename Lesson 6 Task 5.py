# �������-5: ����������� ����� Stationery (������������ ��������������).
# ���������� � ��� ������� title (��������) � ����� draw (���������).
# ����� ������� ��������� ������� ���������.�
# ������� ��� �������� ������ Pen (�����), Pencil (��������), Handle (������).
# � ������ �� ������� ����������� ��������������� ������ draw.
# ��� ������� �� ������� ������ ������ �������� ���������� ���������.
# ������� ���������� ������� � ���������, ��� ������� ��������� ����� ��� ������� ����������.

class Stationery:
    atr_title = 'Title'
    def draw(self):
        print('������ ���������.')
class Pen(Stationery):
    def draw(self):
        print('��������� ������')
class Pencil(Stationery):
    def draw(self):
        print('��������� ����������')
class Handle(Stationery):
    def draw(self):
        print('��������� ��������')

my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()