USE [PELICULA]
GO
/****** Object:  Table [dbo].[CINTAS]    Script Date: 21/12/2023 01:57:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CINTAS](
	[CodCinta] [char](10) NOT NULL,
	[Titulo_Cinta] [varchar](30) NOT NULL,
	[Genero] [varchar](50) NULL,
	[Año] [char](4) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[CodCinta] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[CINTAS] ([CodCinta], [Titulo_Cinta], [Genero], [Año]) VALUES (N'CINTA001  ', N'Noche Terror', N'Suspenso', N'1998')
INSERT [dbo].[CINTAS] ([CodCinta], [Titulo_Cinta], [Genero], [Año]) VALUES (N'CINTA002  ', N'Cartel De Medellin', N'Accion,Violencia', N'1889')
INSERT [dbo].[CINTAS] ([CodCinta], [Titulo_Cinta], [Genero], [Año]) VALUES (N'CINTA003  ', N'Cartel Medellin', N'Drama,Suspenso', N'2012')
GO
