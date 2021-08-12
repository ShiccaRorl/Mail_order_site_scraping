# -*- coding:utf-8 -*-

# 2021/08/08


class Rakuma_Test
    def initialize()

        @path = ARGV[0]
        @data = []
        File.open(@path + "/ラクマ出品一覧.txt", "r:utf-8") do |f|
            @data = f.read().split("\n")
        end

        二重登録チェック()
        ソートする()
    end

    def ソートする()
        begin
            File.open(@path + "/ラクマ出品一覧.txt", "r:utf-8") do |f|
                @data = f.read().split("\n")
            end
            @data.sort!
            File.open(@path + "/ラクマ出品一覧.txt", "w:utf-8") do |f|
                f.write(@data)
            end
        end

        begin
            File.open(@path + "/ラクマ出品一覧Ruby.txt", "r:utf-8") do |f|
                @data = f.read().split("\n")
            end
            @data.sort!
            File.open(@path + "/ラクマ出品一覧Ruby.txt", "w:utf-8") do |f|
                f.write(@data)
            end
        end

        begin
            File.open(@path + "/ラクマディレクトリ.txt", "r:utf-8") do |f|
                @data = f.read().split("\n")
            end
            @data.sort!
            File.open(@path + "/ラクマディレクトリ.txt", "w:utf-8") do |f|
                f.write(@data)
            end
        rescue
            t = 0
            Dir.glob("**/*.txt").each{|i|
                if t == 0 then
                    File.open(@path + "/ラクマディレクトリ.txt", "w:utf-8") do |f|
                        f.write(i + "\n")
                    end
                    t = 1
                else
                    File.open(@path + "/ラクマディレクトリ.txt", "a:utf-8") do |f|
                        f.write(i + "\n")
                    end
                end
            }
        end

        begin
            File.open(@path + "/ラクマ出品一覧在庫1.txt", "r:utf-8") do |f|
                @data = f.read().split("\n")
            end
            @data.sort!
            File.open(@path + "/ラクマ出品一覧在庫1.txt", "w:utf-8") do |f|
                f.write(@data)
            end
        end

        begin
            File.open(@path + "/ラクマ出品一覧在庫0.txt", "r:utf-8") do |f|
                @data = f.read().split("\n")
            end
            @data.sort!
            File.open(@path + "/ラクマ出品一覧在庫0.txt", "w:utf-8") do |f|
                f.write(@data)
            end
        end

        begin
            File.open(@path + "/ラクマ出品一覧２重登録.txt", "r:utf-8") do |f|
                @data = f.read().split("\n")
            end
            @data.sort!
            File.open(@path + "/ラクマ出品一覧２重登録.txt", "w:utf-8") do |f|
                f.write(@data)
            end
        end

        begin
            File.open(@path + "/登録出来ていない商品かも.txt", "r:utf-8") do |f|
                @data = f.read().split("\n")
            end
            @data.sort!
            File.open(@path + "/登録出来ていない商品かも.txt", "w:utf-8") do |f|
                f.write(@data)
            end
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



            #dsize = data.size()
            #data = data - [i]
            #d = (dsize - data.size)
=begin
            if d == 0 then
                if s == 0 then
                    File.open("./ラクマ出品一覧２重登録.txt", "w:utf-8") do |f|
                        f.write(d.to_s + "\n")
                        f.write(data.join("\n"))
                        f.write("\n")
                    end
                    s = 1
                else
                    File.open("./ラクマ出品一覧２重登録.txt", "a:utf-8") do |f|
                        f.write(d.to_s + "\n")
                        f.write(data.join("\n"))
                        f.write("\n")
                    end
                end
            elsif d == 1 then
                    #p "|||||||||||||||||"
            else
                p "================"
                p (dsize - data.size).to_s + "\n"
                p "dsize      :" + dsize.to_s
                p "data.size  :" + data.size.to_s
            end
=end
        }
        p @data.select{|v| @data.count(v) > 1}.uniq

        p @data.group_by{|i| i}.reject{|k,v| v.one?}.keys

    end
end

rakuma_test = Rakuma_Test.new()
 