﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define l = Character('Лера', color="#e24fea")
define ne = Character('Незнакомец', color="#627b93")
define ma = Character('Мама', color="#dc3434")
define d = Character('Даня', color="#e87517")
define a = Character('Артём', color="#384794")
define b = Character('Богдан', color="#d1cb26")
define v = Character('Володя', color="#3c26d1") 

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    
    
    l "[Иногда мне кажется, что люди которые ездят на маршрутке - роботы.]"
    
    l "[Они всегда смотрят в одну точку, будь это телефон или какой-нибудь предмет, лишь изредко поглядавая в окно, что бы посмотреть, не пропустили ли они остановку.]"
    
    l "[Посмотрев в окно, я увидела знакомое место. Мы с матерью уже бывали здесь, когда я заполняла документы по вопросам заселения.]"
    
    l "[Заведующая отделением показалось мне милой женщиной и очень добродушной, с который легко найти общий язык.]"
    
    l "[Наконец, набравшись смелости, я сказала заветную фразу...]"
    
    l "На Ленской, пожалуйста!"
    
    l "[Господи. Как же некомфортно вставать с места, когда с обоих сторон зажали бабки, коса смотрящие на тебя, как на проститутку.]"
    
    l "[Так и хотелось, сказать им что-нибудь обидное, но я пересилила себя и направилась в выходу.]" 
    
    l "[Подходя к водителю, меня окликнул парень.]"
    
    ne "Девушка, вы обронили."
    
    l "[Он протянул мне кошелек.]"
    
    l "Спасибо!"
    
    l "[Ахринеть. Если бы в первый день самостоятельной жизни я потеряла кошелек - мать с отцом меня прибили и забрали обратно в Куйтун.]"
    
    l "[Не то что там плохо, просто все мои одноклассники разъехались по городам, а я бы сидела на одном месте и до конца своей жизни пахала в огороде, каждый вечер встречая своего мужа алкаша с очередной смены.]"
    
    l "[Милый парень, другой бы на его месте оставил себе, без зазрения совести.]"
    
    l "[Дура... Почему я с ним не познакомилась?]"
    
    l "[Проблемы с коммуникабельностью у меня возникли еще в младших классах, когда все сидели по парам, а я одна на задней парте в соляного дрочилась]"
    
    l "[Он побежал в сторону торг сервис, подобие здешнего рынка, крича в телефон: 'Володя, чья очередь хлеб покупать?']"
    
    l "[Мой взгляд с этого парня отвлек звук из моей сумки.]"
    
#ЗВОНОК
    
    ma "Доча, ты добралась?"
    
    l "Да, мам. Я доехала до общаги, сейчас уже пойду к заведующей."
    
    ma "Хорошо. Как заселишься, сразу положи продукты в холодильник, а то испорятся."
    
    l "Знаю, не маленькая."
    
    ma "Ладно, ладно. Позвони как вещи разберешь."
    
    l "Хорошо."
    
    ma "Кстати, отец тебе положил деньги в папку с документами, оплати на них общежитие на пару месяцев вперед."
    
    l "Хорошо, мамуль, целую."
    
    ma "Давай, целую."
    
    l "[Как же бесит, когда мама думает, что ты ничего не можешь сделать без нее]"
    
    
    
    
    
    

    
    


    
    

    return
