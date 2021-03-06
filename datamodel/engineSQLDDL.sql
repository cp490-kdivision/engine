/****** Object:  User [userPerson]    Script Date: 4/20/2021 5:42:14 PM ******/
CREATE USER [userPerson] FOR LOGIN [user123] WITH DEFAULT_SCHEMA=[dbo]
GO
sys.sp_addrolemember @rolename = N'db_datareader', @membername = N'userPerson'
GO
sys.sp_addrolemember @rolename = N'db_datawriter', @membername = N'userPerson'
GO
/****** Object:  Table [dbo].[Characters]    Script Date: 4/20/2021 5:42:14 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Characters](
	[chacracters_ID] [varchar](50) NOT NULL,
	[game_ID] [varchar](50) NULL,
	[location_ID] [varchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[chacracters_ID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ConfitionArg]    Script Date: 4/20/2021 5:42:15 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ConfitionArg](
	[condition_ID] [varchar](50) NULL,
	[condition_Primitive] [varchar](50) NULL,
	[condition_Arg] [varchar](50) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Event_Condition]    Script Date: 4/20/2021 5:42:15 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Event_Condition](
	[condition_ID] [varchar](50) NOT NULL,
	[event_ID] [varchar](50) NULL,
	[condition_Primitive] [varchar](200) NULL,
PRIMARY KEY CLUSTERED 
(
	[condition_ID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Events]    Script Date: 4/20/2021 5:42:15 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Events](
	[event_ID] [varchar](50) NOT NULL,
	[game_ID] [varchar](50) NULL,
	[event_Name] [varchar](50) NULL,
	[event_Condition] [varchar](200) NULL,
PRIMARY KEY CLUSTERED 
(
	[event_ID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Events_False]    Script Date: 4/20/2021 5:42:15 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Events_False](
	[false_ID] [varchar](50) NOT NULL,
	[event_ID] [varchar](50) NULL,
	[false_Position] [varchar](200) NULL,
	[false_Primitive] [varchar](200) NULL,
PRIMARY KEY CLUSTERED 
(
	[false_ID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Events_True]    Script Date: 4/20/2021 5:42:15 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Events_True](
	[true_ID] [varchar](50) NOT NULL,
	[event_ID] [varchar](50) NULL,
	[true_Position] [varchar](200) NULL,
	[true_Primitive] [varchar](200) NULL,
PRIMARY KEY CLUSTERED 
(
	[true_ID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[FalseArg]    Script Date: 4/20/2021 5:42:15 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[FalseArg](
	[false_ID] [varchar](50) NULL,
	[false_Primitive] [varchar](50) NULL,
	[false_Arg] [varchar](50) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Game]    Script Date: 4/20/2021 5:42:15 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Game](
	[game_ID] [varchar](50) NOT NULL,
	[game_Name] [varchar](50) NULL,
	[game_Description] [varchar](256) NULL,
PRIMARY KEY CLUSTERED 
(
	[game_ID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Items]    Script Date: 4/20/2021 5:42:15 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Items](
	[items_ID] [varchar](50) NOT NULL,
	[game_ID] [varchar](50) NULL,
	[location_ID] [varchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[items_ID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[sysdiagrams]    Script Date: 4/20/2021 5:42:15 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[sysdiagrams](
	[name] [sysname] NOT NULL,
	[principal_id] [int] NOT NULL,
	[diagram_id] [int] IDENTITY(1,1) NOT NULL,
	[version] [int] NULL,
	[definition] [varbinary](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[diagram_id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [UK_principal_name] UNIQUE NONCLUSTERED 
(
	[principal_id] ASC,
	[name] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TrueArg]    Script Date: 4/20/2021 5:42:15 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TrueArg](
	[true_ID] [varchar](50) NULL,
	[true_Primitive] [varchar](50) NULL,
	[true_Arg] [varchar](100) NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Characters]  WITH CHECK ADD FOREIGN KEY([game_ID])
REFERENCES [dbo].[Game] ([game_ID])
GO
ALTER TABLE [dbo].[ConfitionArg]  WITH CHECK ADD FOREIGN KEY([condition_ID])
REFERENCES [dbo].[Event_Condition] ([condition_ID])
GO
ALTER TABLE [dbo].[Event_Condition]  WITH CHECK ADD FOREIGN KEY([event_ID])
REFERENCES [dbo].[Events] ([event_ID])
GO
ALTER TABLE [dbo].[Events]  WITH CHECK ADD FOREIGN KEY([game_ID])
REFERENCES [dbo].[Game] ([game_ID])
GO
ALTER TABLE [dbo].[Events_False]  WITH CHECK ADD FOREIGN KEY([event_ID])
REFERENCES [dbo].[Events] ([event_ID])
GO
ALTER TABLE [dbo].[Events_True]  WITH CHECK ADD FOREIGN KEY([event_ID])
REFERENCES [dbo].[Events] ([event_ID])
GO
ALTER TABLE [dbo].[FalseArg]  WITH CHECK ADD FOREIGN KEY([false_ID])
REFERENCES [dbo].[Events_False] ([false_ID])
GO
ALTER TABLE [dbo].[Items]  WITH CHECK ADD FOREIGN KEY([game_ID])
REFERENCES [dbo].[Game] ([game_ID])
GO
ALTER TABLE [dbo].[TrueArg]  WITH CHECK ADD FOREIGN KEY([true_ID])
REFERENCES [dbo].[Events_True] ([true_ID])
GO
