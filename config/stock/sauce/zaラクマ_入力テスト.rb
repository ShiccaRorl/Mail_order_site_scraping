# -*- coding:utf-8 -*-

# 2021/08/08

ROOT_PATH = 'C:/Users/user/Downloads/バックアップ/プログラム/バックアップ/保存/メルカリ'


class Rakuma_Test
    def initialize()

        @path = ARGV[0]
        @data = []
        File.open(@path + "/ラクマ出品一覧.txt", "r:utf-8") do |f|
            @data = f.read().split("\n")
        end

        二重登録チェック()
        #ソートする()
    end

    def ソートする()
        begin
            File.open(@path + "/ラクマ出品一覧.txt", "r:utf-8") do |f|
                @data = f.read().split("\n")
            end
            @data.sort!
            i = 0
            @data.each{|data|
                if i == 0 then
                    File.open(@path + "/ラクマ出品一覧.txt", "w:utf-8") do |f|
                        f.write(data + "\n")
                        i = 1
                    end
                else
                    File.open(@path + "/ラクマ出品一覧.txt", "a:utf-8") do |f|
                        f.write(data + "\n")
                    end
                end
            }
        end

        begin
            File.open(@path + "/ラクマ出品一覧Ruby.txt", "r:utf-8") do |f|
                @data = f.read().split("\n")
            end
            @data.sort!
            i = 0
            @data.each{|data|
                if i == 0 then
                    File.open(@path + "/ラクマ出品一覧Ruby.txt", "w:utf-8") do |f|
                        f.write(data + "\n")
                        i = 1
                    end
                else
                    File.open(@path + "/ラクマ出品一覧Ruby.txt", "a:utf-8") do |f|
                        f.write(data + "\n")
                    end
                end
            }
        end

        begin
=begin
            File.open("./ラクマディレクトリ.txt", "r:utf-8") do |f|
                @data = f.read().split("\n")
            end
            @data.sort!
            i = 0
            @data.each{|data|
                if i == 0 then
                    File.open("./ラクマディレクトリ.txt", "w:utf-8") do |f|
                        f.write(data + "\n")
                        i = 1
                    end
                else
                    File.open("./ラクマディレクトリ.txt", "a:utf-8") do |f|
                        f.write(data + "\n")
                    end
                end
            }
=end
            t = 0
            Dir.glob(ROOT_PATH + "/**/*.txt").each{|i|
                if t == 0 then
                    File.open("./ラクマディレクトリ.txt", "w:utf-8") do |f|
                        f.write(i + "\n")
                    end
                    t = 1
                else
                    File.open("./ラクマディレクトリ.txt", "a:utf-8") do |f|
                        f.write(i + "\n")
                    end
                end
            }
            File.open("./ラクマディレクトリ.txt", "r:utf-8") do |f|
                @data = f.read().split("\n")
            end
            @data.sort!
            File.open("./ラクマディレクトリ.txt", "w:utf-8") do |f|
                f.write(@data)
            end
		rescue
			
        end

        begin
            File.open(@path + "/ラクマ出品一覧在庫1.txt", "r:utf-8") do |f|
                @data = f.read().split("\n")
            end
            @data.sort!
            i = 0
            @data.each{|data|
                if i == 0 then
                    File.open(@path + "/ラクマ出品一覧在庫1.txt", "w:utf-8") do |f|
                        f.write(data + "\n")
                        i = 1
                    end
                else
                    File.open(@path + "/ラクマ出品一覧在庫1.txt", "a:utf-8") do |f|
                        f.write(data + "\n")
                    end
                end
            }
        end

        begin
            File.open(@path + "/ラクマ出品一覧在庫0.txt", "r:utf-8") do |f|
                @data = f.read().split("\n")
            end
            @data.sort!
            i = 0
            @data.each{|data|
                if i == 0 then
                    File.open(@path + "/ラクマ出品一覧在庫0.txt", "w:utf-8") do |f|
                        f.write(data + "\n")
                        i = 1
                    end
                else
                    File.open(@path + "/ラクマ出品一覧在庫0.txt", "a:utf-8") do |f|
                        f.write(data + "\n")
                    end
                end
            }
        end

        begin
            File.open(@path + "/ラクマ出品一覧２重登録.txt", "r:utf-8") do |f|
                @data = f.read().split("\n")
            end
            @data.sort!
            i = 0
            @data.each{|data|
                if i == 0 then
                    File.open(@path + "/ラクマ出品一覧２重登録.txt", "w:utf-8") do |f|
                        f.write(data + "\n")
                        i = 1
                    end
                else
                    File.open(@path + "/ラクマ出品一覧２重登録.txt", "a:utf-8") do |f|
                        f.write(data + "\n")
                    end
                end
            }
        end

        begin
            File.open(@path + "/登録出来ていない商品かも.txt", "r:utf-8") do |f|
                @data = f.read().split("\n")
            end
            @data.sort!
            i = 0
            @data.each{|data|
                if i == 0 then
                    File.open(@path + "/登録出来ていない商品かも.txt", "w:utf-8") do |f|
                        f.write(data + "\n")
                        i = 1
                    end
                else
                    File.open(@path + "/登録出来ていない商品かも.txt", "a:utf-8") do |f|
                        f.write(data + "\n")
                    end
                end
            }
        end

        begin
            File.open(@path + "/出品されているのに在庫0のリスト.txt", "r:utf-8") do |f|
                @data = f.read().split("\n")
            end
            @data.sort!
            i = 0
            @data.each{|data|
                if i == 0 then
                    File.open(@path + "/出品されているのに在庫0のリスト.txt", "w:utf-8") do |f|
                        f.write(data + "\n")
                        i = 1
                    end
                else
                    File.open(@path + "/出品されているのに在庫0のリスト.txt", "a:utf-8") do |f|
                        f.write(data + "\n")
                    end
                end
            }
        end
    end

    def 二重登録チェック()
        data = @data
        dammy = @data
        dammy.uniq!

        s = 0
        #dsize = data.size()
        dammy.each{|i|
            if s == 0 then
                File.open(@path + "/ラクマ出品一覧Ruby.txt", "w:utf-8") do |f|
                    f.write(i + "\n")
                end
                s = 1
            else
                File.open(@path + "/ラクマ出品一覧Ruby.txt", "a:utf-8") do |f|
                    f.write(i + "\n")
                end
            end
        }
    end
end

rakuma_test = Rakuma_Test.new()
 