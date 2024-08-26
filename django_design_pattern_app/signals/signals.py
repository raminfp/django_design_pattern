from django import dispatch


user_visit_signal = dispatch.Signal(["date_time","ip","device"])
