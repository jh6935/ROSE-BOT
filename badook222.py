import discord
#본 봇은 대화 봇입니다.
#바둑이 봇이며, 맨 아래 bot.run ()부분에 봇 토큰을 넣으세요.
#코드를 2차 배포는 깃허브 링크만 가능합니다.
#이 코드를 사용할 시 봇 소개메시지에 출처를 남겨주시면 감사하겠습니다.
#대화 이외 기능은 없다는 점 알아두시면 감사하겠습니다.
#제작자 크레딧
# 디스코드: https://discord.gg/Uu6xpf7Wha (바둑이 서포트 및 테스트 서버)
# 제작자 DM: 대니#6385
# 접두사 사용 법 바둑아 부분을 원하는 접두사로 바꿔주세요. 접두사 바둑이가 없는 경우 바꾸지 말아주세요.
class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("개발")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("준비가 완료되었습니다. 이제 봇을 사용할 수 있습니다.")

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message, cc=1):
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        if message.author.bot:
            return None

        # message.content = message의 내용
        if message.content == "장미야 대니":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "대니는 웨이브소프의 창업자이고 JH,제로의 온라인 친구이기도 해요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        #message.content = message의 내용
        if message.content == "장미야 안녕":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕하세요."
            msg2 = "장미봇입니당!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        #message.content = message의 내용
        if message.content == "장미야 뭐해":
            # 현재 채널을 받아
            channel = message.channel
            # 답변 내용 구성
            msg = "간식을 뜯으면서 자요!(?)"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None


        #message.content = message의 내용
        if message.content == "장미야 앉아":
            channel = message.channel
            # 답변 내용 구성
            msg = "월 월 그르릉"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        #message.content = message의 내용
        if message.content == "장미야 씨발":
            channel = message.channel
            # 답변 내용 구성
            msg = "ㅠㅠㅠㅠㅠㅠㅠ왈 왈 왈 크르릉..."
            await channel.send(msg)
            return None

        #message.content = message의 내용
        if message.content == "장미야 어글리":
            channel = message.channel
            msg = "스크래치 잘하는 스크래쳐에요! GL소프트를 운영중이기도하답니당!"
            await channel.send(msg)
            return None

        if message.content == "장미야 뭐먹지?":
            channel = message.channel
            msg = "역시 라면이 답이죵~ 저는 삼양라면을 추천해요!"
            await channel.send(msg)
            return None

        if message.content == "장미야":
            channel = message.channel
            msg = "넵 주인님"
            await channel.send(msg)
            return None

        if message.content == "장미야 출첵":
            channel = message.channel
            cc = +1
            msg = "출첵이 완료되었어요."
            await channel.send(msg)
            return None


        if message.content == "장미야 출첵횟수":
            channel = message.channel
            msg = "열심히 개발중이랍니당"
            await channel.send(msg)
            return None

        if message.content == "장미야 배고파":
            channel = message.channel
            msg = "개껌을 씹으세요!"
            msg2 = "그런의미로 개껌하나 주시는거 어때요 >.<"
            await channel.send(msg)
            await channel.send(msg2)
            return None

        if message.content == "장미야 노조":
            channel =message.channel
            msg = "나쁜노조때무네 하루도 잘 넘어가질 않아여! 부들부들"
            await channel.send(msg)
            return None

        if message.content == "병신":
            channel = message.channel
            msg = "흐음 개가5이면 그중1개는 병신이죠 훠훠"
            await channel.send(msg)
            return None


        if message.content == "장미야 병신":
            channel = message.channel
            msg = "크르렁 왈왈!!!!!"
            await channel.send(msg)
            return None


        if message.content == "장미야 씨발":
            channel = message.channel
            msg = "뭐라구여 바보똥꺠 멍충이놈이!"
            await channel.send(msg)
            return None

        if message.content == "장미야 자살":
            channel = message.channel
            msg = "1393 전화해서 똑같은말하세용~"
            await channel.send(msg)
            return None

        if message.content == "장미야 밥줄께":
            channel = message.channel
            msg = "와작와작 마시따"
            await channel.send(msg)
            return None


        if message.content == "장미야 섹스":
            channel = message.channel
            msg = "왈왈 왈(뭔소리하는지 개가 어캐 알아들음?)"
            await channel.send(msg)
            return None


        if message.content == "섹스":
            channel = message.channel
            msg = "왈왈 왈(뭔소리하는지 개가 어캐 알아들음?)"
            await channel.send(msg)
            return None

        if message.content == "장미야 바둑이":
            channel = message.channel
            msg = "바둑이는 저의 사촌이에여!"
            await channel.send(msg)
            return None


        if message.content == "장미야 고기":
            channel = message.channel
            msg = "마시는 고기 나도줘 왈왈!"
            await channel.send(msg)
            return None

        if message.content == "장미야 정보":
            channel = message.channel
            msg = "저는 바둑이봇을 기본베이스로 만들어진 귀여운 강아지 봇이랍니당"
            await channel.send(msg)
            return None

        if message.content == "장미야 JH":
            channel = message.channel
            msg = "저의 주인님입니당"
            await channel.send(msg)
            return None

        if message.content == "장미야 제로":
            channel = message.channel
            msg = "제로는 가끔 제작자가 질투하기도하는 스치OS 잘만드는 미국유학파 인간입니다!"
            await channel.send(msg)
            return None

        if message.content == "장미야 스크래치":
            channel = message.channel
            msg = "마냥이 좋아할거 같은데;"
            await channel.send(msg)
            return None

        if message.content == "장미야 파이썬":
            channel = message.channel
            msg = "개발자가 뛰어쓰기 때무네 괭장히 혐오하는 언어!"
            await channel.send(msg)
            return None

        if message.content == "장미야 물어와":
            channel = message.channel
            msg = "왈왈"
            await channel.send(msg)
            return None

        if message.content == "장미야 방탄소년단":
            channel = message.channel
            msg = "방탄? 방탄하면 유리지 ㅇㅈ?"
            await channel.send(msg)
            return None

        if message.content == "장미야 BTS":
            channel = message.channel
            msg = "버터스???"
            await channel.send(msg)
            return None

        if message.content == "장미야 엔트리":
            channel = message.channel
            msg = "스크래치인데 구림 ㄹㅇㅋㅋ"
            await channel.send(msg)
            return None

        if message.content == "바둑아 장미":
            channel = message.channel
            msg = "나 불렀쪄?"
            await channel.send(msg)
            return None

        if message.content == "장미야 어쩔티비":
            channel = message.channel
            msg = "저쩔티비"
            msg2 = "저쩔냉장고"
            msg3 = "저쩔 로봇청소공기청정기"
            await channel.send(msg)
            return None

        if message.content == "장미야 바보":
            channel = message.channel
            msg = "왈?"
            await channel.send(msg)
            return None

        if message.content == "장미야 개쌔끼":
            channel = message.channel
            msg = "다큰 개라고요!"
            await channel.send(msg)
            return None

        if message.content == "장미야 버그":
            channel = message.channel
            msg = "거부"
            await channel.send(msg)
            return None

        if message.content == "장미야 사람":
            channel = message.channel
            msg = "나는 고라...아니 강아지~~"
            await channel.send(msg)
            return None

        if message.content == "장미야 물어와":
            channel = message.channel
            msg = "왈왈~~"
            await channel.send(msg)
            return None







##여기부터 검열기능
        @bot.event
async def on_message(message): # 메세지가 채널에 올라왔을 때 (해당 매세지)
    message_content = message.content # 메세지 내용을 message_content라는 변수에 담고
    bad = message_content.find("바둑아") # 메세지 내용 중 바둑아이란 단어가 있다면 0 이상을 반환
    print(bad)
    if bad >= 0:
        await message.delete() # 욕설이 담긴 메세지를 삭제합니다.
    await bot.process_commands(message) # 메세지 중 명령어가 있을 경우 처리해주는 코드







        

# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run("OTYxMjUzMzIzNTM1Njg3NzAw.Yk2S6w.7lSbEqpgQkxT1IKdtB-HJnSf3UQ")

#봇 코드 마지막 줄입니다. 여기까지가 코드입니다. (총 296줄)
