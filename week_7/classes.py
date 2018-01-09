from datetime import datetime


class point:
    """Creates a point with X, Y attributes"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def slope_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distance(self, target):
        return ((target.x - self.x)**2 + (target.y - self.y)**2)**0.5

    def reflect_x(self):
        reflect_x = point(self.x, self.y * -1)
        return reflect_x

    def get_line(self, target):
        slope = (target.y - self.y) / (target.x - self.x)
        y_int = self.y - (slope * self.x)
        return (slope, y_int)


class rectangle:
    """Creates a rectangle object at point(X,Y)"""

    def __init__(self, posn=point(), width=0, height=0):
        self.posn = posn
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def flip(self):
        self.width, self.height = self.height, self. width

    def contains(self, target):
        return (target.x < (self.posn.x + self.width)) and (target.x >= self.posn.x) \
            and (target.y < (self.posn.y + self.height)) and (target.y >= self.posn.y)

    def __str__(self):
        return "{}, {}x{}".format(self.posn, self. width, self.height)


# r1 = rectangle(point(3, 9), 10, 5)
# print(r1.contains(point(3, 9)))
# print(r1.contains(point(3, 5)))
# print(r1.contains(point(13, 10)))
# print(r1.contains(point(12, 14)))
# print(r1.contains(point(12.99, 13.999)))
# p1 = point(3, 9)
# p2 = point(8, 6)

# # print(p1, p2)
# # print(round(p1.distance(p2), 3))
# # print(p1.reflect_x())
# # print(p2.slope_from_origin())
# print("With points {0} and {1} the formula is: Y = {2:.1f}x + {3:.1f}"
#       .format(p1, p2, p1.get_line(p2)[0], p1.get_line(p2)[1]))


# class sms_store:
#     '''Creates SMS tuple with different methods'''

#     message_count = 0
#     inbox = []

#     def __init__(self, has_been_viewed=False, date_time="", text=""):
#         self.has_been_viewed = False
#         self.date_time = date_time
#         self.text = text
#         sms_store.message_count += 1
#         sms_store.inbox.append(self)

#     def __str__(self):
#         self.has_been_viewed = True
#         return "'{}' {} ".format(self.text, self.date_time)

#     @staticmethod
#     def unread_messages():
#         unread = 0
#         for message in sms_store.inbox:
#             if message.has_been_viewed == False:
#                 unread += 1
#         return unread

#     @classmethod
#     def delete_message(cls, index):
#         deleted = sms_store.inbox.pop(index)
#         print("Deleting message {}, {}".format(
#             index + 1, deleted.text))
#         deleted.text = None
#         deleted.date_time = None
#         deleted.has_been_viewed = None


# sms_1 = sms_store(False, str(datetime.now()), "Hey!")
# sms_2 = sms_store(False, str(datetime.now()), "HeyYYYYYY!")
# sms_3 = sms_store(False, str(datetime.now()), "Answer Me!")


# print(sms_store.unread_messages())
# sms_store.delete_message(1)
# print(sms_2)
# print(sms_store.unread_messages())
