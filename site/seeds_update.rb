# -*- encoding: utf-8 -*-
#! snap/bin/ruby

# gem install sequel
# gem install sqlite3

require "sqlite3"
require "sequel"

options = {:encoding=>"utf8"}
#DBに接続
begin
    @db = Sequel.sqlite("./../../db.sqlite3", options)
rescue
    print("メインのDBが開かない\n")
end

@db[:seeds].where(:id=>ARGV[0]).update(:analysis_completed=>true, :update_at=>Time.now)
@db[:seeds].where(:id=>ARGV[0]).delete
