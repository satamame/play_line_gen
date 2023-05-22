from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

load_dotenv()


def make_prompt():
    plot = ''\
        '時間のループに囚われた4人が、そのことに気づいて謎を解く話。'\
        '誰かが麻薬性鎮痛薬を飲むと時間が劇の冒頭に戻る。'\
        '時間が戻ると全員の記憶もその時点に戻る。'\
        '時間が戻ってもセットや小道具や衣装に付いた血液はリセットされない。'
    scene_plot = ''\
        'まだ誰も時間がループしていることに気づいていない。'\
        '宝来と生名が江原田にいたずらをしようとしている。'\
        'そのいたずらとは、江原田に時間がループしていると信じさせようというもの。'\
        '宝来と生名はこの会話をしたことがあると言って江原田を騙そうとする。'
    preceding_lines = ''\
        '@宝来\nもう何回もこの会話をしているのよ。\n\n'\
        '@生名\n江原田さんは憶えていないんですか？\n\n'\
        '@宝来\n人によってループの記憶があったりなかったりするのかしら。\n\n'
    who_says = '江原田'
    character = ''\
        '20歳。女性。画家。内気な性格で口数が少なく、いつもオドオドしている。'\
        '落ち着きがないが、考え方は論理的。'\
        '言葉遣いは非常に丁寧で基本的に「ですます調」で話す。'
    what_to_say = ''\
        '自分はこの会話をするのは初めてなので、にわかには信じられないと言う。'\
        'ただ、時間がループしている可能性も完全には否定できないと考察する。'\
        'また、時間がループしていることの確実な根拠はないか、宝来と生名に質問する。'

    template = ''\
        '劇の台本を書いています。以下の情報を元に次のセリフを書いてください。\n\n'\
        '劇のあらすじ: """\n{plot}\n"""\n'\
        '今のシーンのあらすじ: """\n{scene_plot}\n"""\n'\
        '直前のセリフ: """\n{preceding_lines}\n"""\n'\
        '次のセリフを言う人: {who_says}\n'\
        '{who_says}のキャラクタ: """\n{character}\n"""\n'\
        'セリフで何を言うか: """\n{what_to_say}\n"""'

    prmp = PromptTemplate(
        input_variables=[
            'plot', 'scene_plot', 'preceding_lines', 'who_says', 'character',
            'what_to_say'
        ],
        template=template,
    )

    return prmp.format(
        plot=plot,
        scene_plot=scene_plot,
        preceding_lines=preceding_lines,
        who_says=who_says,
        character=character,
        what_to_say=what_to_say,
    )


def main():
    llm = OpenAI(temperature=0.9)

    prmp = make_prompt()

    # print(f'prmp:\n{prmp}\n')

    print(llm(prmp))


if __name__ == '__main__':
    main()
