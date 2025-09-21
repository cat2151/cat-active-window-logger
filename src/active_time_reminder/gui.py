"""
アクティブ時間リマインダー GUI モジュール

このモジュールは、アクティブ時間リマインダー機能のためのシンプルなTkinterベースのGUIを提供します。
GUIは非ブロッキング設計なので、メインプロセスから呼び出すことができます。
"""

import tkinter as tk
from tkinter import ttk


class ActiveTimeReminderGUI:
    """アクティブ時間リマインダーのためのシンプルなGUIウィンドウ。"""

    def __init__(self, title="Active Time Reminder"):
        """
        GUIウィンドウを初期化します。

        Args:
            title (str): ウィンドウタイトル
        """
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("400x300")
        self.root.resizable(True, True)

        # UIコンポーネントを初期化
        self._setup_ui()

        # ウィンドウが実行中かどうかを追跡するフラグ
        self.is_running = False

    def _setup_ui(self):
        """ユーザーインターフェースコンポーネントをセットアップします。"""
        # メインフレーム
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # レスポンシブデザインのためのグリッド重みを設定
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # タイトルラベル
        title_label = ttk.Label(
            main_frame,
            text="Active Time Reminder",
            font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, pady=(0, 20))

        # ステータスフレーム
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="10")
        status_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        status_frame.columnconfigure(0, weight=1)

        # ステータスラベル
        self.status_label = ttk.Label(
            status_frame,
            text="Ready",
            font=("Arial", 12)
        )
        self.status_label.grid(row=0, column=0, pady=5)

        # コントロールボタンフレーム
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, pady=10)

        # 開始/停止ボタン
        self.control_button = ttk.Button(
            button_frame,
            text="Start",
            command=self._toggle_reminder
        )
        self.control_button.pack(side=tk.LEFT, padx=5)

        # 閉じるボタン
        close_button = ttk.Button(
            button_frame,
            text="Close",
            command=self.close
        )
        close_button.pack(side=tk.LEFT, padx=5)

    def _toggle_reminder(self):
        """リマインダーのオン/オフを切り替えます。"""
        if self.is_running:
            self.stop_reminder()
        else:
            self.start_reminder()

    def start_reminder(self):
        """リマインダー機能を開始します。"""
        self.is_running = True
        self.status_label.config(text="Running")
        self.control_button.config(text="Stop")
        print("Reminder started")  # 実際の機能のプレースホルダー

    def stop_reminder(self):
        """リマインダー機能を停止します。"""
        self.is_running = False
        self.status_label.config(text="Stopped")
        self.control_button.config(text="Start")
        print("Reminder stopped")  # 実際の機能のプレースホルダー

    def show(self):
        """ウィンドウを表示します（非ブロッキング）。"""
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()

    def hide(self):
        """ウィンドウを隠します。"""
        self.root.withdraw()

    def close(self):
        """ウィンドウを閉じてクリーンアップします。"""
        if self.is_running:
            self.stop_reminder()
        self.root.quit()
        self.root.destroy()

    def update(self):
        """
        GUIを更新します（非ブロッキング）。
        このメソッドはメインループから定期的に呼び出される必要があります。
        """
        try:
            self.root.update_idletasks()
            self.root.update()
        except tk.TclError:
            # ウィンドウが閉じられた
            return False
        return True

    def run_blocking(self):
        """GUIをブロッキングモードで実行します（スタンドアロン実行用）。"""
        self.root.mainloop()


def main():
    """スタンドアロン実行用のメイン関数。"""
    gui = ActiveTimeReminderGUI()

    # ウィンドウクローズイベントを処理
    def on_closing():
        gui.close()

    gui.root.protocol("WM_DELETE_WINDOW", on_closing)

    # スタンドアロン実行用のブロッキングモードで実行
    gui.run_blocking()


if __name__ == "__main__":
    main()
