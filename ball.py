
class Ball:
    """ ボールクラス
    円を描く関数を使って表現する。
    """
    
    def __init__(self, canvas, color):
        """ 初期化処理
        メイン側から Canvas を受け取る。
        ボールの色も str 型で受け取る。
        """
        self.canvas = canvas
        # 楕円を描く関数できれいな円を描画する。識別番号を保持しておく。
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)
        # 画面サイズ(縦/横)を取得しておく。
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        # ボールの初期位置を計算で決める。リセット時のことを考えて保存しておく。
        self.init_x = self.canvas_width / 2 - 7.5
        self.init_y = self.canvas_height / 2 - 7.5
        # ボールの移動スピードをとりあえず0で作っておく
        self.speed = 0
        # ボールのx/yのスピードを0でとりあえず初期化
        self.x = 0
        self.y = 0
        
        # ボール始動
        self.start()

    def start(self):
        # 初期位置へ移動(絶対座標)
        self.canvas.moveto(self.id, self.init_x, self.init_y)
        self.speed = 3      # 初期スピード
        """ 発射角度のリストを生成(angle の処理内容)
            1 - range() で 20 - 60 のデータを作成
            2 - list() でリスト型に変換
            3 - random.choice() でリストから1個をランダムで選択
            4 - math.radians() で度数法から弧度法(ラジアン)に変換
        """
        angle = math.radians(random.choice(list(range(20, 65, 5))))
        direction = random.choice([1, -1])  # xの向きをランダムに。
        # 三角関数をつかって、x軸y軸それぞれの移動速度を求める。
        self.x = math.cos(angle) * self.speed * direction
        self.y = math.sin(angle) * self.speed
    
    def draw(self):
        # ボールを移動させる
        self.canvas.move(self.id, self.x, self.y)











    